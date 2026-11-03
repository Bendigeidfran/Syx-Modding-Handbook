"""MkDocs hook: turns a sprite sheet image into an interactive sheet.

A page shows a sheet as an ordinary image on a line of its own. If a file with
the same name and the extension ".sections" sits beside the image, this hook
adds a raised, hoverable section over the image for each of its lines:

    name | x, y, width, height | The text for the tooltip.

The position is in the image's own pixels. The button stays still and covers its
part of the image while its art lifts, so a section is only ever drawn once. The
tooltip text goes in attributes, which the search index doesn't read.

These tooltips are only on the site for now. The PDF prints the plain image.

A section outside the image or a malformed line is logged as a warning, which
makes "mkdocs build --strict" fail.
"""
import html
import logging
import os
import posixpath
import re
import struct

log = logging.getLogger("mkdocs.site_sheets")

MAX_WIDTH = 680
MAX_HEIGHT = 1000
MAX_ZOOM = 4

IMAGE = re.compile(r'<p><img alt="(?P<alt>[^"]*)" src="(?P<src>[^"]+)"\s*/?></p>')
POSITION = re.compile(r"^(\d+),\s*(\d+),\s*(\d+),\s*(\d+)$")


def _png_size(path):
    with open(path, "rb") as fh:
        head = fh.read(24)
    if head[:8] != b"\x89PNG\r\n\x1a\n":
        return None
    return struct.unpack(">II", head[16:24])


def _percent(value):
    return f"{value:.4f}".rstrip("0").rstrip(".") + "%"


def _part(src, title, tip, x, y, w, h, width, height):
    position = f"{x}, {y}, {w}, {h}"
    # An unnamed section's title already is its position.
    shown = "" if title == position else position
    # Sizing and placing the same image so that it shows only this section.
    size_x = width / w * 100
    size_y = height / h * 100
    pos_x = x / (width - w) * 100 if width != w else 0
    pos_y = y / (height - h) * 100 if height != h else 0
    place = (
        f"left:{_percent(x / width * 100)};top:{_percent(y / height * 100)};"
        f"width:{_percent(w / width * 100)};height:{_percent(h / height * 100)}"
    )
    art = (
        f"background-image:url('{src}');"
        f"background-size:{_percent(size_x)} {_percent(size_y)};"
        f"background-position:{_percent(pos_x)} {_percent(pos_y)}"
    )
    label = html.escape(f"{title}{' at ' + shown if shown else ''}: {tip}", quote=True)
    return (
        f'<button type="button" class="sheet-part" style="{place}" aria-label="{label}" '
        f'data-title="{html.escape(title, quote=True)}" data-pos="{shown}" data-tip="{html.escape(tip, quote=True)}">'
        f'<span class="sheet-art" style="{art}"></span></button>'
    )


def _sections(path, where, width, height):
    parts = []
    with open(path, encoding="utf-8") as fh:
        for number, line in enumerate(fh, 1):
            line = line.strip()
            if not line:
                continue
            cells = [c.strip() for c in line.split("|")]
            found = POSITION.match(cells[1]) if len(cells) == 3 else None
            if not found:
                log.warning("%s line %d: must be name | x, y, width, height | text", path, number)
                continue
            x, y, w, h = map(int, found.groups())
            if w == 0 or h == 0 or x + w > width or y + h > height:
                log.warning("%s: %s: %s is outside the %d x %d image", where, cells[0], cells[1], width, height)
                continue
            parts.append((cells[0], cells[2], x, y, w, h))
    return parts


def on_page_content(content, page, config, files):
    if "<img" not in content:
        return content

    def build(match):
        src = match.group("src")
        if re.match(r"^[a-z]+:", src):
            return match.group(0)
        dest = posixpath.normpath(posixpath.join(posixpath.dirname(page.file.dest_uri), src))
        image = next((f for f in files if f.dest_uri == dest), None)
        if image is None:
            return match.group(0)
        path = os.path.splitext(image.abs_src_path)[0] + ".sections"
        if not os.path.exists(path):
            return match.group(0)

        where = page.file.src_uri
        size = _png_size(image.abs_src_path)
        if size is None:
            log.warning("%s: sheet image is not a PNG: %s", where, src)
            return match.group(0)
        width, height = size

        parts = [
            _part(src, title, tip, x, y, w, h, width, height)
            for title, tip, x, y, w, h in _sections(path, where, width, height)
        ]
        # A whole-number zoom keeps the pixels crisp.
        zoom = max(1, min(MAX_ZOOM, MAX_WIDTH // width, MAX_HEIGHT // height))
        return (
            f'<figure class="sheet" style="width:{width * zoom}px">'
            f'<img alt="{match.group("alt")}" src="{src}" width="{width}" height="{height}">'
            f'{"".join(parts)}</figure>'
        )

    return IMAGE.sub(build, content)
