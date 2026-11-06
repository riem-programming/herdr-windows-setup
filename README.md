# herdr on Windows 11

A small, reproducible setup of [herdr](https://herdr.dev) (terminal workspace manager for AI coding agents) on Windows 11, using Windows Terminal, the Claude Code integration, and three native terminal tools: lazygit, glow and yazi.

Every keybinding comes from herdr's prefix mode (`ctrl+b` + key). One source of truth, no key translation layers.

## Quick path

1. Install herdr (PowerShell):
   ```powershell
   powershell -ExecutionPolicy Bypass -c "irm https://herdr.dev/install.ps1 | iex"
   ```
   Fallback: `curl.exe -fsSLo install.cmd https://herdr.dev/install.cmd && install.cmd && del install.cmd`
2. Install the Claude Code integration: `herdr integration install claude`
3. Install the tools: `winget install JesseDuffield.lazygit charmbracelet.glow sxyazi.yazi`
4. Copy the files from [`config/`](config) to the locations below.
5. Add [`herdr-profile.json`](config/windows-terminal/herdr-profile.json) to `profiles.list` in Windows Terminal settings.
6. Run `herdr`. Reload config later with `herdr server reload-config`.

| File in this repo | Destination |
|-------------------|-------------|
| `config/herdr/config.toml` | `%APPDATA%\herdr\config.toml` |
| `config/yazi/yazi.toml`, `keymap.toml` | `%APPDATA%\yazi\config\` |
| `config/glow/glow.yml`, `style.json` | `%LOCALAPPDATA%\glow\Config\` (edit the absolute `style` path) |
| `config/windows-terminal/herdr-profile.json` | Windows Terminal `profiles.list` entry |

## Environment

| Component | Version |
|-----------|---------|
| Windows 11 | build 26200 |
| Windows Terminal | 1.24 |
| PowerShell | 7.6 (herdr's default pane shell when `pwsh` is on PATH) |
| herdr | 0.9.5 (stable), Claude Code integration v11 |
| lazygit / glow / yazi | 0.66.1 / 3.0.0 / 26.9.1 (winget) |

## Keybindings

All start with `ctrl+b`. `ctrl+b ?` shows the full list. Detach with `ctrl+b q` (everything keeps running).

| Keys | Action |
|------|--------|
| `ctrl+b g` | Goto: pane finder (herdr built-in) |
| `ctrl+b z` | Zoom the focused pane |
| `ctrl+b alt+g` | lazygit, typed into the focused pane |
| `ctrl+b alt+m` | glow (markdown reader) in a temporary pane |
| `ctrl+b alt+f` | yazi (file browser) in a temporary pane |
| `ctrl+b shift+g` | Git worktrees (not set up yet) |

## Docs

| Doc | Content |
|-----|---------|
| [concepts](docs/concepts.md) | Server/client, workspaces, panes, agent states, persistence |
| [decisions](docs/decisions.md) | Why Windows Terminal, prefix-only keys, no plugins, no Neovim |
| [tools](docs/tools.md) | lazygit, glow, yazi: setup and cheat sheets |
| [troubleshooting](docs/troubleshooting.md) | Known limitations and fixes |
| [next-steps](docs/next-steps.md) | Pending tests and ideas |

## Claude Code integration

`herdr integration install claude` writes `~/.claude/hooks/herdr-agent-state.ps1` and adds a `SessionStart` hook entry to `~/.claude/settings.json` (matcher `^(startup|resume|clear|compact|fork)$`).

- The hook exits immediately unless `HERDR_ENV=1`, so it only runs inside herdr.
- It only reports the Claude session id. After a restart herdr uses it to run `claude --resume <id>`.

The hook script and settings file are not included in this repo.
