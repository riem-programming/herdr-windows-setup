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

### Validating `theme.toml`

A timed launch of yazi does not report config errors when its output is redirected, so it is not a validator. Check keys against the official JSON schema instead:

```powershell
curl.exe -fsSLo theme-schema.json https://yazi-rs.github.io/schemas/theme.json
python -I scripts/check-yazi-theme.py theme-schema.json "$env:APPDATA\yazi\config\theme.toml"
```

It reports every section or key that the schema does not know. The final check is still opening yazi: a bad file prints "Failed to parse config".

## delta

Syntax-highlighted diffs with line numbers. Used as the first diff renderer in lazygit (`config/lazygit/config.yml`, `git.diffRenderers`; press `|` in lazygit to cycle renderers). `--syntax-theme ansi` keeps it on the terminal's 16 colors.

To use it for plain `git diff` / `git show` too, merge `config/git/delta.gitconfig` into `~/.gitconfig`:

```powershell
git config --global core.pager delta
git config --global interactive.diffFilter "delta --color-only"
git config --global delta.navigate true
git config --global delta.line-numbers true
git config --global delta.syntax-theme ansi
git config --global merge.conflictstyle zdiff3
```

## zoxide

Remembers the directories you visit and jumps by name: `z herdr`, `z api`, `zi` (interactive). Needs one line in the PowerShell profile (`config/powershell/profile-snippet.ps1`). yazi's built-in `z` key uses the zoxide database once zoxide is installed.

## bat

`cat` with syntax highlighting, line numbers and git change markers. Config in `config/bat/config` (`--theme="ansi"` follows the terminal scheme). Try `bat README.md`, `bat -A file` (show whitespace), `bat --diff file`.

## eza

`ls` replacement: `eza -l --git --icons` (git status per file), `eza --tree --level 2`, `eza -la --sort modified`. Icons use the Nerd Font. No config.

## sd

Find and replace without sed syntax: `sd 'old' 'new' file`, `sd -p 'old' 'new' file` (preview only), capture groups with `$1`. No config.
