# 🌌 CAD Auto Wiki

Welcome! CAD Auto is a single-file browser app (`index.html`) for CAD
automation, styled with the FBK Checker design system.

## Pages

- 🎨 [Design System](Design-System.md) — colors, typography, components
- 🛰️ [Version Badge](Version-Badge.md) — the space emoji that changes every push
- 🔭 [Workflow](Workflow.md) — branches, checks, pushing
- 🤖 [AI Instructions](../CLAUDE.md) — rules every AI assistant follows

## App layout

```
┌──────────────────────────────────────────────────────────────┐
│ CAD · AUTOMATION   [no file]      ↥ Load  ⊡ Fit  ↓ Export 🚀 │  ← .bar (navy, gold rule)
├───────────────────────────────────────────────┬──────────────┤
│ ⬚                                             │ INSPECTOR    │
│ ✥            canvas stage (.stage)            │  .kv rows    │
│                                               ├──────────────┤
│ [hud]                                         │ LOG  (n)     │
└───────────────────────────────────────────────┴──────────────┘
```

On screens narrower than 840px the inspector hides and the canvas fills the
width.
