# 🚀 CAD Auto

A single-file browser app for CAD automation, built on the same navy-and-gold
UI as **FBK Checker**. No install, no build step: open `index.html` in a
browser.

**Draft from aerial:** drag a box on the aerial map and CAD Auto drafts the
curb lines and building footprints inside it. It traces the curbs
automatically from the aerial image, or takes them from OpenStreetMap or your
ArcGIS layers, in Ramsey County feet, shows them in a CAD
view, and exports a DXF. See [Draft From Aerial](wiki/Draft-From-Aerial.md).

## Quick start

```bash
git clone https://github.com/joaogoncalvescstp-oss/Cad-auto.git
cd Cad-auto
# open index.html in your browser, or serve it:
python3 -m http.server 8000   # then visit http://localhost:8000
```

## Version badge 🪐

The top-right badge shows a **space emoji + build number** (hover it for the
build). It changes on every push, so if the badge matches the latest push you
know you're not looking at a cached page. History lives in
[`CLAUDE.md`](CLAUDE.md#build-history).

## Docs

| | |
|---|---|
| 📖 [Wiki home](wiki/Home.md) | Overview and links |
| 🛰️ [Draft from aerial](wiki/Draft-From-Aerial.md) | Select area → curb + building lines → DXF |
| 🎨 [Design system](wiki/Design-System.md) | Colors, type, components (from FBK Checker) |
| 🛰️ [Version badge](wiki/Version-Badge.md) | How the space emoji rotation works |
| 🔭 [Workflow](wiki/Workflow.md) | Branches, verifying, pushing |
| 🤖 [AI instructions](CLAUDE.md) | Standing rules for AI assistants ([AGENTS.md](AGENTS.md)) |

## Project layout

```
index.html            the app (HTML + CSS + JS inline)
wiki/                 project wiki
tools/bump_space.py   bumps the space badge each push
CLAUDE.md / AGENTS.md AI assistant instructions
```
