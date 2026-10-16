# CAD Auto — Standing Notes for AI Assistants

Notes from the owner so they don't get forgotten between sessions. Read this
first and follow it on every task in this repo.

## Standing rules (always do these)

- **Bump the space version badge on EVERY push.** Use a *different* space
  emoji each time (next one in the list below) and increment `build`. This lets
  the owner confirm the live page isn't cached.
  - Easiest: run `python3 tools/bump_space.py "short note of what changed"`.
    It updates both places in `index.html` and appends a row to the history
    table below.
  - By hand, update BOTH places in `index.html`:
    1. The static badge span (`id="spaceBadge"`) text in the top bar.
    2. The `const VERSION={emoji,name,build}` marker in the script
       (search for `VERSION MARKER`).
  - Tell the owner which emoji + build you pushed so they can check it live.
- **Keep `main` and the working branch in sync.** The owner wants every push
  reflected on `main`.
- **Keep the UI on the shared design system** (see `wiki/Design-System.md`).
  It is the same navy/gold look as FBK Checker — reuse its CSS tokens and
  component classes (`.bar`, `.btn`, `.btn.gold`, `.pill`, `.tool`, `.side`,
  `.kv`, `.le`) instead of inventing new styles.
- **Verify the inline script parses before pushing**, e.g.
  `node -e "const h=require('fs').readFileSync('index.html','utf8');new Function(h.split('<script>')[1].split('</script>')[0])"`.
- **Update the wiki** (`wiki/`) when a feature or workflow changes.

## Space emoji rotation

In order; after the last one, wrap back to the top.

🚀 ROCKET · 🪐 SATURN · 🌙 MOON · ☄️ COMET · 🛰️ SATELLITE · 🌌 GALAXY ·
🌠 SHOOTING STAR · 👽 ALIEN · 🛸 UFO · 🌍 EARTH · ☀️ SUN · ⭐ STAR ·
🔭 TELESCOPE · 🧑‍🚀 ASTRONAUT · 🌕 FULL MOON · 🌑 NEW MOON · 💫 STARDUST ·
🌎 AMERICAS · 🌏 ASIA · ✨ SPARKLES · 🌗 HALF MOON · 🌒 CRESCENT

## Build history

| Build | Emoji | Note |
|-------|-------|------|
| 1 | 🚀 ROCKET | repo setup: main branch, README, wiki, AI instructions, FBK-style UI shell |
| 2 | 🪐 SATURN | aerial map: select area → draft curb + building CAD lines (OSM or ArcGIS layer) → CAD view + DXF export (Ramsey Co. ft) |

## Project layout

- `index.html` — single-file app (HTML + CSS + JS inline), no build step.
- `wiki/` — project wiki (Markdown, GitHub-renderable).
- `tools/bump_space.py` — bumps the space badge + history table.
- `CLAUDE.md` — this file (AI instructions). `AGENTS.md` points here.

## Workflow

1. Make the change in `index.html` (or wherever it belongs).
2. Verify the script parses (see above).
3. `python3 tools/bump_space.py "what changed"`.
4. Commit, push the working branch, and fast-forward `main` to match.
