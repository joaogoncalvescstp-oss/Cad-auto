# 🌌 CAD Auto Wiki

Welcome! CAD Auto is a single-file browser app (`index.html`) for CAD
automation, styled with the FBK Checker design system.

## Pages

- 🛰️ [Draft From Aerial](Draft-From-Aerial.md): select an area, draft curb and building lines, export DXF
- 🎨 [Design System](Design-System.md) — colors, typography, components
- 🛰️ [Version Badge](Version-Badge.md) — the space emoji that changes every push
- 🔭 [Workflow](Workflow.md) — branches, checks, pushing
- 🤖 [AI Instructions](../CLAUDE.md) — rules every AI assistant follows

## App layout

```
┌──────────────────────────────────────────────────────────────────────┐
│ CAD · AUTOMATION [n curb · n bldg]  🛰Aerial|📐CAD ⊡Fit ✕Clear ↓DXF 🚀 │  ← .bar
├───────────────────────────────────────────────────────┬──────────────┤
│ ▭  select box                              legend     │ DRAFT FROM   │
│ ⛶  use visible map                                    │ 1 Area       │
│        aerial map (Leaflet)  /  CAD canvas            │ 2 Layers     │
│                                                       │ 3 Output     │
│ [hud: E/N]                                    +/−     │ LOG (n)      │
└───────────────────────────────────────────────────────┴──────────────┘
```

On screens narrower than 840px the side panel moves below the map.
