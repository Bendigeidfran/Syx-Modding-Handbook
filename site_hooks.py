"""MkDocs hooks for the handbook site.

The handbook keeps the PDF's file layout: a "00-" page is its folder's title
page. These hooks make MkDocs treat those pages as folder index pages, and name
each nav section after its title page. They change navigation, URLs and
markup only, never the text of a page, so the site and the PDF stay identical.

Facts tables are written with an empty header row (| | |) and a label in each
row's first cell. For screen readers, the empty header row is dropped and each
first cell becomes a row header, so a value is announced with its label.

MkDocs lists a folder's files before its sub-folders, so the nav is set
explicitly to the PDF's order: a depth-first walk sorted by name, as in
collect() in tools/build_pdf.py.
"""
import os
import posixpath
import re
from pathlib import PurePosixPath

from mkdocs.utils import nest_paths


def on_files(files, config):
    pages = files.documentation_pages()
    config.nav = nest_paths(sorted((f.src_uri for f in pages), key=lambda p: PurePosixPath(p).parts))
    for f in pages:
        if posixpath.basename(f.src_uri).startswith("00-"):
            # 00-Welcome.md -> index.html, 01-init/00-init.md -> 01-init/index.html
            f.name = "index"
            f.dest_uri = posixpath.join(posixpath.dirname(f.src_uri), "index.html")
            f.url = f._get_url()
            f.abs_dest_path = os.path.normpath(os.path.join(f.dest_dir, f.dest_uri))
    return files


def _title(file):
    match = re.search(r"^#\s+(.+)$", file.content_string, re.M)
    return match.group(1).strip().strip("`") if match else None


def on_nav(nav, config, files):
    def walk(items):
        for item in items:
            if item.is_section:
                index = next((c for c in item.children if c.is_page and c.file.name == "index"), None)
                if index is not None:
                    item.title = _title(index.file) or item.title
                walk(item.children)

    walk(nav.items)
    return nav


EMPTY_HEAD = re.compile(r"<thead>\s*<tr>\s*(?:<th[^>]*>\s*</th>\s*)+</tr>\s*</thead>\s*")
TABLE = re.compile(r"<table>(?:(?!</table>).)*</table>", re.S)
FIRST_CELL = re.compile(r"(<tr>\s*)<td([^>]*)>(.*?)</td>", re.S)


def _facts_table(match):
    table = match.group(0)
    if not EMPTY_HEAD.search(table):
        return table
    table = EMPTY_HEAD.sub("", table, count=1)
    return FIRST_CELL.sub(r'\1<th scope="row"\2>\3</th>', table)


def on_page_content(content, page, config, files):
    if "<thead>" not in content:
        return content
    return TABLE.sub(_facts_table, content)
