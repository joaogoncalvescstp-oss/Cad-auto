# 🛰️ Version Badge

Every push changes the emoji in the top-right corner of the app. If the badge
you see matches the one announced for the latest push, your browser isn't
showing a cached copy. (FBK Checker does the same with fruit; CAD Auto uses
space.)

- Hover the badge for the build number. Click it for a little spin.
- The value lives in two places in `index.html`: the `#spaceBadge` span and
  `const VERSION={emoji,name,build}` (search `VERSION MARKER`).

## Bumping it

```bash
python3 tools/bump_space.py "what changed in this push"
```

This picks the next emoji in the rotation, increments the build, updates
`index.html`, and adds a row to the build history in `CLAUDE.md`.

## Rotation

🚀 ROCKET → 🪐 SATURN → 🌙 MOON → ☄️ COMET → 🛰️ SATELLITE → 🌌 GALAXY →
🌠 SHOOTING STAR → 👽 ALIEN → 🛸 UFO → 🌍 EARTH → ☀️ SUN → ⭐ STAR →
🔭 TELESCOPE → 🧑‍🚀 ASTRONAUT → 🌕 FULL MOON → 🌑 NEW MOON → 💫 STARDUST →
🌎 AMERICAS → 🌏 ASIA → ✨ SPARKLES → 🌗 HALF MOON → 🌒 CRESCENT → (back to 🚀)
