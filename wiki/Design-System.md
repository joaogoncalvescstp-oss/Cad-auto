# 🎨 Design System

Taken from **FBK Checker** so both apps look and feel the same. Everything is
defined as CSS variables on `:root` in `index.html`.

## Colors

| Token | Value | Use |
|-------|-------|-----|
| `--navy` / `--navy2` | `#071D49` / `#0c2a66` | Top bar gradient |
| `--gold` | `#F1B434` | Accent: bar rule, primary buttons, headings, counters |
| `--gold-dim` | `#b8861f` | Hover borders, focus rings |
| `--bg` | `#0a0f1c` | Page background |
| `--panel` / `--panel2` | `#0f1626` / `#131c30` | Side panel / inputs and cards |
| `--rule` | `#22304d` | Borders and dividers |
| `--ink` / `--mut` | `#e8edf6` / `#8a99b8` | Main text / muted text |
| `--grid` | `#16203a` | Canvas grid lines |
| `--pass` / `--warn` / `--fail` | `#35c184` / `#f0b429` / `#ff5d52` | Status |
| `--pt` / `--ctrl` | `#7fb3ff` / `#ffd24a` | Points / control points |

## Type

- UI text: `"Segoe UI", system-ui, sans-serif`, 14px.
- Labels, buttons, numbers: `--mono` (`ui-monospace, "Cascadia Code", Consolas`).
- Section headings (`.side h3`): 10px mono, uppercase, `letter-spacing:.18em`, gold.

## Components

| Class | What it is |
|-------|-----------|
| `.bar` | Top bar — navy gradient, 3px gold bottom border, scrolls sideways on mobile |
| `.brand .k` / `.brand .t` | Tiny gold uppercase kicker + bold app title |
| `.btn` | Default button (dark navy) |
| `.btn.gold` | Primary action |
| `.btn.ghost` | Transparent secondary action |
| `.file` | Wraps an `<input type=file>` to look like a `.btn` |
| `.pill` | Rounded status chip (e.g. current file name) |
| `.tool` / `.tool.on` | 40×40 floating canvas tool; gold when active |
| `.hud` | Bottom-left status readout over the canvas |
| `.side` | Right inspector panel (320px) |
| `.kv` | Key/value row in the inspector |
| `.log` / `.le` | Change log list with a gold counter badge `.n` |
| `#spaceBadge` | Version badge — see [Version Badge](Version-Badge.md) |

## Rules of thumb

- Gold means "primary" or "active" — use it sparingly.
- Icons are plain Unicode glyphs in buttons (`↥ ↓ ⊡ ↶ ↷ ⚙`), no icon font.
- Add new colors as `:root` tokens, never as one-off hex values in rules.
