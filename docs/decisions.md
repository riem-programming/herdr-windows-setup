# Decisions

ADR-style: one section per decision.

## 0. Guiding principle: stable and verified on Windows first

- **Rule:** Only use tools and features that are documented as supported on native Windows and that we have verified ourselves. Do not add anything that is marked preview, experimental, best-effort, or that assumes Unix tooling (`sh`, `bash`, `$EDITOR`, Unix paths), even if it works today.
- **Context:** Windows is not the primary platform for most terminal tooling. Plugins, layouts and mods from the herdr gallery are "preview / best-effort" on Windows and many shell out to `sh`/`bash`. The previous setup broke repeatedly for exactly this reason.
- **How to apply:**
  - Before adding a tool or setting, check the herdr Windows support page and the tool's own Windows notes.
  - Prefer single-binary tools with native Windows builds (lazygit, glow, yazi) over plugins.
  - Prefer herdr's built-in features (themes, keybindings, custom commands) over gallery plugins.
  - One `experimental` setting is allowed only when its failure mode is harmless: `pane_history` (worst case, a pane restores empty).
  - Validate every config change (`herdr server reload-config` with no diagnostics, tool launches cleanly) before committing it here.
- **Consequences:** Fewer features, zero surprises. If something is not stable on Windows, the answer is "not yet", not "let's patch around it".

## 1. Rebuild from scratch

- **Context:** The previous setup was herdr 0.9.3 + WezTerm + WezTerm SendKey bindings that translated `Ctrl+T` etc. into herdr `ctrl+alt` chords + Git Bash launcher scripts. It grew by trial and error (7 config backups) and had two sources of truth for keybindings.
- **Decision:** Uninstall everything and rebuild with a minimal config.
- **Consequences:** Less to maintain; the config in [`config/`](../config) is the whole setup.

## 2. Windows Terminal as the outer terminal

- **Context:** The herdr Windows docs list "Windows Terminal / PowerShell app attach" as supported. WezTerm is only verified through WSL.
- **Decision:** Use Windows Terminal with a dedicated `herdr` profile. It is not the default profile, so a plain PowerShell is always available to fix things if herdr fails.
- **Consequences:** No Kitty graphics, so `terminal.kitty_graphics = false`.

## 3. Prefix-mode keybindings only

- **Context:** Two keybinding layers (terminal and herdr) caused confusion.
- **Decision:** Use only herdr prefix mode (`ctrl+b` + key). `ctrl+b ?` lists everything.
- **Consequences:** One source of truth. Custom binds only when a real pain appears. `prefix+g` is herdr's built-in goto and is not overridden.

## 4. Hybrid workflow: herdr + lazygit + VS Code

- **Context:** Agents work in small steps that need review.
- **Decision:** herdr runs and monitors agents. lazygit reviews diffs and commits after each small AI step. VS Code handles large diffs, markdown with images and file browsing when preferred.
- **Consequences:** Three tools with clear roles instead of one overloaded editor.

## 5. No Neovim

- **Context:** Neovim needs heavy configuration on Windows and many plugins assume Unix tooling.
- **Decision:** Not used. VS Code (`code` on PATH) is the editor.
- **Consequences:** yazi must define its editor opener explicitly (see [tools](tools.md)).

## 6. Native terminal tools instead of gallery plugins

- **Context:** herdr plugins on Windows are "preview / best-effort", and many use `sh`/`bash`.
- **Decision:** Skip gallery plugins, layouts and mods. Use lazygit, glow and yazi.
- **Consequences:** Less magic, but each tool is wired by a plain custom command.

## 7. Custom command types

| Type | Behavior | Used for |
|------|----------|----------|
| `shell` | Detached command | lazygit (`herdr pane run` into the focused pane) |
| `pane` | Temporary pane, closes on exit | glow, yazi |
| `popup` | Modal, fixed size, cannot be zoomed, not a pane | Not used |

On Windows these run via `cmd.exe /d /c`, hence the `%VAR%` syntax.

## Config reference

| Setting | Value | Why |
|---------|-------|-----|
| `onboarding` | `false` | Skip the first-run wizard |
| `ui.toast.delivery` | `"system"` | Windows notification center (`off`, `herdr`, `terminal`, `system`) |
| `ui.sound.enabled` | `true` | Done chime and needs-input alert, only for background workspaces |
| `session.resume_agents_on_restore` | `true` | Default, explicit |
| `experimental.pane_history` | `true` | Restore pane screen content after restart |
| `terminal.kitty_graphics` | `false` | Windows Terminal lacks Kitty graphics |

Print the full reference with `herdr --default-config`.
