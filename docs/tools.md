# Tools

Installed with `winget install JesseDuffield.lazygit charmbracelet.glow sxyazi.yazi`.

## lazygit

Launched with `ctrl+b alt+g`. It types `lazygit` into the **focused** pane (no split), so focus a shell pane first. Otherwise the text goes to whatever runs there, for example Claude.

| Key | Action |
|-----|--------|
| `space` | Stage / unstage |
| `c` | Commit |
| `?` | Help |
| `q` | Quit |

Practice: commit after each AI step. Write short conventional commit messages that say why.

## glow

Launched with `ctrl+b alt+m` (temporary pane, closes on exit).

| Setting | Value | Why |
|---------|-------|-----|
| `tui` | `true` | A file argument opens the scrollable reader instead of printing and exiting |
| `style` | custom `style.json` | Removes literal `##` heading prefixes, adds table separators |
| `width` | `120` | More room for tables |

Wide tables still wrap. Use VS Code preview for those.

**Appearance:** lazygit inherits the terminal's 16 ANSI colors (Minimal Ink scheme), so it needs no theme. glow defines its own colors, so `style.json` carries the Minimalism palette.

`glow.yml` needs an **absolute** `style` path; the copy in this repo uses `%LOCALAPPDATA%` as a placeholder. Replace it with your real path.

## yazi

Launched with `ctrl+b alt+f` (temporary pane, `ctrl+b z` to zoom).

**Appearance:** yazi defines its own colors, so `theme.toml` carries the Minimalism palette (lazygit needs no theme: it inherits the terminal's 16 ANSI colors).

Windows has no `$EDITOR`, so the openers are explicit:

| Opener | Command | Notes |
|--------|---------|-------|
| `edit` | `code %s` | `orphan`: VS Code outlives yazi |
| `read` | `glow %s` | `block`: glow owns the screen until `q` |

| Rule (first match wins) | Opens with |
|-------------------------|------------|
| `*.md` | `[read, edit]`: `Enter` = glow, `O` = open-with menu |
| `text/*`, json, toml, yaml, source extensions | VS Code |

Gotchas:

- Rule order matters: `*.md` must precede `text/*`.
- Rule keys are `url` / `mime`, not `name`.
- `Shift+Enter` is mapped to `shell 'code %s' --orphan`: always VS Code.

| Key | Action |
|-----|--------|
| `a` | Create (trailing `/` = directory) |
| `r` | Rename |
| `y` / `x` / `p` | Copy / cut / paste |
| `d` / `D` | Trash / delete permanently |
| `Enter` | Open |
| `Tab` | File info |
| `.` | Toggle hidden files |
| `~` | Help |
