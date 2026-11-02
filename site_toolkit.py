"""MkDocs hooks that publish toolkit/tags.json.

The Songs of Syx Modding Toolkit shows the Compendium's tag descriptions in its
file editor. This reads the pages as they are and writes those descriptions out
as data, so pages keep the format that suits human readers. It never changes a
page, so the site and the PDF stay identical.

A tag is a tag-shaped ### or #### heading, or a row in a table whose first column
is "Tag", in a section that holds tags: "## Tags" and "## The text file", plus
any named in PAGE_MAP. Anything the file would get wrong is logged as a warning,
which makes "mkdocs build --strict" fail.
"""
import hashlib
import json
import logging
import os
import re

from markdown.extensions.toc import slugify, unique

log = logging.getLogger("mkdocs.site_toolkit")

COMPENDIUM = "04-Modding-Compendium/"
WELCOME = "00-Welcome.md"
OUTPUT = os.path.join("toolkit", "tags.json")
SCHEMA = 1

# Exceptions, for pages that aren't one file described under "## Tags". Keys are
# paths inside the Compendium. Each can set:
#   location: the file or folder, for a page with no Location row of its own
#   sections: "## heading" -> a path prefix for its tags ("" for none), or a dict
#             with any of prefix, location, and text (true for text file tags)
#   paths:    tag name in a heading or table -> the full path, or a list of paths
#   flatten:  true if #### tags leave out their ### parent, because it repeats
#             the same tags under different names (such as the seasons)
#   key_tables: true if tables whose first column is "Key" also list tags, with
#             the facts table at the top of the section applying to each
_ACTION_GROUPS = (
    "How actions are written",
    "Events",
    "Boosts",
    "Money and resources",
    "Your population",
    "Other factions",
    "Disasters and the world",
    "Appearance and sound",
)
PAGE_MAP = {
    "01-init/02-battle/01-divType.md": {
        "paths": {t: f"TYPES.{t}" for t in ("OCCURENCE", "TRAININGS", "EQUIPMENT")},
    },
    "01-init/03-config/04-DefaultProjectile.md": {"flatten": True, "sections": {"Tags": "PROJECTILE"}},
    "01-init/03-config/06-GenerationSettlement.md": {"sections": {"Tags": "GENERATION"}},
    "01-init/03-config/08-LEAVE_CAUSE.md": {"key_tables": True},
    "01-init/03-config/14-Time.md": {"flatten": True},
    "01-init/03-config/07-LAW.md": {"sections": {"Crimes": "CRIMES", "Punishments": "PUNISHMENTS"}},
    "01-init/04-disease.md": {"sections": {"The config file": {"location": "assets/init/disease/_CONFIG.txt"}}},
    "01-init/05-event/00-event.md": {"sections": {"_CONFIG.txt": {"location": "assets/init/event/_CONFIG.txt"}}},
    "01-init/05-event/01-structure.md": {"location": "assets/init/event/"},
    "01-init/05-event/02-occurrence.md": {"location": "assets/init/event/", "sections": {"OCCURENCE": "OCCURENCE"}},
    "01-init/05-event/03-actions.md": {"location": "assets/init/event/", "sections": dict.fromkeys(_ACTION_GROUPS, "")},
    "01-init/05-event/04-text.md": {"location": "assets/text/event/"},
    "01-init/07-race/02-preferences.md": {"location": "assets/init/race/", "sections": {"Tags": "PREFERRED"}},
    "01-init/07-race/03-stats.md": {"location": "assets/init/race/", "sections": {"Format": "STATS"}},
    "01-init/07-race/06-sprite/00-sprite.md": {
        "sections": {"Name-set files": {"location": "assets/text/names/nameset/"}},
    },
    "01-init/07-race/06-sprite/01-colours-and-extras.md": {
        "location": "assets/init/race/sprite/",
        "sections": {"Headwear": "", "Colours": ""},
        "paths": {t: [f"{w}.{t}" for w in ("CROWN", "MERC", "RAIDER")] for t in ("FILE", "OFFX", "OFFY")},
    },
    "01-init/07-race/06-sprite/02-types-and-faces.md": {
        "location": "assets/init/race/sprite/",
        "sections": {"TYPES": "TYPES", "Type tags": "TYPES", "Face parts": "TYPES.FACE", "CHILD": "CHILD"},
    },
    "03-sprite/03-game.md": {"sections": {"Sprite entries": ""}},
}

_NAME = r"[A-Z0-9_*]+(?:\.[A-Z0-9_*]+)*"
TAG_HEADING = re.compile(rf"{_NAME}(?:(?:, {_NAME})*(?:,? and {_NAME})?)$")
LOCATION_ROW = re.compile(r"^\| \*\*Location\*\* \| `([^`]+)`", re.M)
FACTS_ROW = re.compile(r"\*\*([^*]+)\*\*$")
VERSION = re.compile(r"^\*?Written for Songs of Syx v(\d+\.\d+\.\d+)\*?$", re.M)
FACT_NAMES = {"Type": "type", "Range": "range", "Required": "required", "Default": "default", "Effect": "effect"}


def _plain(text):
    """Markdown to plain text: inline code stays, links and emphasis go."""
    parts = re.split(r"(`[^`]*`)", re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", text))
    for i in range(0, len(parts), 2):
        # Bold can span inline code, so its markers are removed one at a time.
        parts[i] = re.sub(r"(?<![\w*])\*([^*\s][^*]*)\*(?![\w*])", r"\1", parts[i].replace("**", ""))
    return "".join(parts).strip()


def _cells(row):
    return [c.strip().replace("\\|", "|") for c in re.split(r"(?<!\\)\|", row.strip().strip("|"))]


def _names(heading):
    return re.split(r", and |, | and ", heading)


def _join(*parts):
    return ".".join(p for p in parts if p)


class _Page:
    def __init__(self, rel, text, mapping, base_url):
        self.mapping = mapping
        self.base_url = base_url
        self.entries = []
        self.problems = []
        self.seen_sections = set()
        self.slugs = set()
        self.anchor = ""
        self.section = None
        self.current = None
        self.parents = []
        self.section_facts = {}
        self.caption = False
        match = LOCATION_ROW.search(text)
        self.location = mapping.get("location") or (match.group(1) if match else None)
        self.sections = {"Tags": "", "The text file": {"text": True}, **mapping.get("sections", {})}
        self._walk(text)
        for name in self.sections:
            if name not in self.seen_sections and name not in ("Tags", "The text file"):
                self.problems.append(f'PAGE_MAP names a section "## {name}" that isn\'t on this page')

    def _mapped(self, name):
        found = self.mapping.get("paths", {}).get(name, name)
        return found if isinstance(found, list) else [found]

    def _new(self, paths, **fields):
        entry = {"paths": paths, "section": self.section, "anchor": self.anchor, "prose": [], "example": None, "facts": {}, **fields}
        self.entries.append(entry)
        return entry

    def _heading(self, level, title):
        title = title.strip()
        self.anchor = unique(slugify(title.replace("`", ""), "-"), self.slugs)
        self.slugs.add(self.anchor)
        if level == 2:
            self.current, self.parents, self.section_facts = None, [], {}
            found = self.sections.get(title, False)
            if found is False:
                self.section = None
                return
            self.seen_sections.add(title)
            found = {"prefix": found} if isinstance(found, str) else found
            self.section = {"prefix": found.get("prefix", ""), "text": found.get("text", False),
                            "location": found.get("location") or self.location}
        elif self.section and level in (3, 4):
            if not TAG_HEADING.match(title):
                # A prose heading: its text isn't a tag's, but its tables may hold tags.
                self.current = None
                if level == 3:
                    self.parents = []
                return
            names = [p for n in _names(title) for p in self._mapped(n)]
            if level == 3:
                self.parents = [_join(self.section["prefix"], n) for n in names]
                # A heading can add the example for a tag that a table row on this page describes.
                row = next((e for e in self.entries if e.get("row") and e["paths"] == self.parents), None)
                self.current = row or self._new(list(self.parents))
            else:
                flat = self.mapping.get("flatten")
                bases = [self.section["prefix"]] if flat or not self.parents else self.parents
                self.current = self._new([_join(b, n) for b in bases for n in names])

    def _table(self, rows):
        header, body = _cells(rows[0]), [_cells(r) for r in rows[2:]]
        if header[0] == "Tag" or (header[0] == "Key" and self.mapping.get("key_tables")):
            for row in body:
                self._tag_row(header, row)
        elif self.current is None:
            # Facts that apply to the whole section, for tags listed in Key tables.
            for row in body:
                label = FACTS_ROW.match(row[0])
                if label and label.group(1) in FACT_NAMES:
                    self.section_facts[FACT_NAMES[label.group(1)]] = _plain(row[1])
        else:
            for row in body:
                label = FACTS_ROW.match(row[0])
                if label and label.group(1) in FACT_NAMES:
                    self.current["facts"][FACT_NAMES[label.group(1)]] = _plain(row[1])
                else:
                    self.current["prose"].append("- " + ": ".join(_plain(c) for c in row))

    def _tag_row(self, header, row):
        names = [p for n in re.findall(r"`([^`]+)`", row[0]) for p in self._mapped(n)]
        bases = self.parents or [self.section["prefix"]]
        labelled = header[0] == "Key"
        facts, text = dict(self.section_facts) if labelled else {}, []
        for head, cell in zip(header[1:], row[1:]):
            cell = _plain(cell)
            if head == "Type and range":
                facts["type"], _, value = cell.partition(", ")
                if value:
                    facts["range"] = value
            elif head in FACT_NAMES:
                facts[FACT_NAMES[head]] = cell
            elif not text and not labelled:
                text.append(cell)
            else:
                text.append(f"{head}: {cell}")
        joined = ". ".join(t.rstrip(".") for t in text) + "." if labelled else " ".join(text)
        self._new([_join(b, n) for b in bases for n in names], prose=[joined], facts=facts, row=True)

    def _walk(self, text):
        lines = text.splitlines()
        i = 0
        while i < len(lines):
            line = lines[i]
            if line.lstrip().startswith("```"):
                fence = line.lstrip()[:3]
                code = []
                i += 1
                while i < len(lines) and not lines[i].lstrip().startswith(fence):
                    code.append(lines[i])
                    i += 1
                if self.section and self.current is not None:
                    # A line introducing the code means nothing without it.
                    if self.current["prose"] and self.current["prose"][-1].endswith(":") and self.caption:
                        self.current["prose"].pop()
                    if self.current["example"] is None:
                        self.current["example"] = "\n".join(code)
            elif re.match(r"#{1,6} ", line):
                self._heading(len(line) - len(line.lstrip("#")), line.lstrip("#"))
            elif self.section and line.startswith("|"):
                start = i
                while i + 1 < len(lines) and lines[i + 1].startswith("|"):
                    i += 1
                self._table(lines[start : i + 1])
                self.caption = False
            elif self.section and self.current is not None and line.strip():
                self.current["prose"].append(_plain(line.lstrip("> ")))
                self.caption = True
                i += 1
                continue
            elif line.strip():
                self.caption = False
            i += 1


def _output(entry, url):
    paragraphs = [p for p in entry["prose"] if p]
    description = "\n\n".join(paragraphs) or None
    facts = entry["facts"]
    return {
        "summary": paragraphs[0] if paragraphs else None,
        "description": description,
        "type": facts.get("type"),
        "range": facts.get("range"),
        "required": facts.get("required"),
        "default": facts.get("default"),
        "effect": facts.get("effect"),
        "unverified": bool(description and re.search(r"Unverified:|TODO:", description)),
        "example": entry["example"],
        "url": f"{url}#{entry['anchor']}",
    }


_state = {}


def build(pages, site_url):
    """pages is (Compendium-relative path, text, page URL) for each page. Returns (locations, problems)."""
    locations, seen, problems = {}, {}, []
    for rel in PAGE_MAP.keys() - {p[0] for p in pages}:
        problems.append(f"PAGE_MAP names a page that doesn't exist: {rel}")
    for rel, text, url in pages:
        page = _Page(rel, text, PAGE_MAP.get(rel, {}), site_url)
        problems.extend(f"{rel}: {p}" for p in page.problems)
        for entry in page.entries:
            location = entry["section"]["location"]
            if not location:
                problems.append(f"{rel}: {entry['paths'][0]} has no Location; add a Location row, or a location in PAGE_MAP")
                continue
            effect = entry["facts"].get("effect")
            if effect not in (None, "None", "Unread"):
                problems.append(f"{rel}: {entry['paths'][0]}: Effect must be exactly None or Unread")
            kind = "text_tags" if entry["section"]["text"] else "tags"
            block = locations.setdefault(location, {"tags": {}, "text_tags": {}})
            for path in entry["paths"]:
                key = (location, kind, path)
                if key in seen:
                    problems.append(f"{rel}: {path} is already documented under {location} on {seen[key]}")
                    continue
                seen[key] = rel
                block[kind][path] = _output(entry, site_url + url)
    return locations, problems


def on_files(files, config):
    _state["files"] = files
    return files


def on_post_build(config):
    pages, version = [], None
    for f in _state["files"].documentation_pages():
        if f.src_uri == WELCOME:
            match = VERSION.search(f.content_string)
            version = match.group(1) if match else None
        elif f.src_uri.startswith(COMPENDIUM):
            pages.append((f.src_uri[len(COMPENDIUM) :], f.content_string, f.url))
    if version is None:
        log.warning(f"{WELCOME}: the line 'Written for Songs of Syx vX.Y.Z' is missing or has changed")
    locations, problems = build(pages, config.site_url)
    for problem in problems:
        log.warning(problem)
    body = json.dumps(locations, sort_keys=True, ensure_ascii=False)
    data = {"schema": SCHEMA, "game_version": version, "content_hash": hashlib.sha256(body.encode("utf-8")).hexdigest(), "locations": locations}
    path = os.path.join(config.site_dir, OUTPUT)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as out:
        json.dump(data, out, sort_keys=True, ensure_ascii=False, indent=1)
