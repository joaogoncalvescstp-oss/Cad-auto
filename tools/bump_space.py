#!/usr/bin/env python3
"""Bump the space version badge: next emoji, build+1, history row in CLAUDE.md.

Usage: python3 tools/bump_space.py "what changed in this push"
"""
import re
import sys
from pathlib import Path

ROTATION = [
    ("🚀", "ROCKET"), ("🪐", "SATURN"), ("🌙", "MOON"), ("☄️", "COMET"),
    ("🛰️", "SATELLITE"), ("🌌", "GALAXY"), ("🌠", "SHOOTING STAR"),
    ("👽", "ALIEN"), ("🛸", "UFO"), ("🌍", "EARTH"), ("☀️", "SUN"),
    ("⭐", "STAR"), ("🔭", "TELESCOPE"), ("🧑‍🚀", "ASTRONAUT"),
    ("🌕", "FULL MOON"), ("🌑", "NEW MOON"), ("💫", "STARDUST"),
    ("🌎", "AMERICAS"), ("🌏", "ASIA"), ("✨", "SPARKLES"),
    ("🌗", "HALF MOON"), ("🌒", "CRESCENT"),
]

ROOT = Path(__file__).resolve().parent.parent
HTML = ROOT / "index.html"
NOTES = ROOT / "CLAUDE.md"
MARKER = re.compile(r"const VERSION=\{emoji:'([^']*)',name:'([^']*)',build:(\d+)\};")
BADGE = re.compile(r'(<span id="spaceBadge"[^>]*>)[^<]*(</span>)')


def main():
    note = " ".join(sys.argv[1:]).strip()
    if not note:
        sys.exit('usage: python3 tools/bump_space.py "what changed"')

    html = HTML.read_text(encoding="utf-8")
    m = MARKER.search(html)
    if not m:
        sys.exit("VERSION marker not found in index.html")
    names = [n for _, n in ROTATION]
    cur = names.index(m.group(2)) if m.group(2) in names else -1
    emoji, name = ROTATION[(cur + 1) % len(ROTATION)]
    build = int(m.group(3)) + 1

    html = MARKER.sub(f"const VERSION={{emoji:'{emoji}',name:'{name}',build:{build}}};", html)
    html, n = BADGE.subn(rf"\g<1>{emoji} {name}\g<2>", html)
    if n != 1:
        sys.exit("spaceBadge span not found in index.html")
    HTML.write_text(html, encoding="utf-8")

    notes = NOTES.read_text(encoding="utf-8")
    rows = list(re.finditer(r"^\| \d+ \|.*\|$", notes, re.M))
    if not rows:
        sys.exit("build history table not found in CLAUDE.md")
    end = rows[-1].end()
    notes = notes[:end] + f"\n| {build} | {emoji} {name} | {note} |" + notes[end:]
    NOTES.write_text(notes, encoding="utf-8")

    print(f"Build {build}: {emoji} {name}")


if __name__ == "__main__":
    main()
