# Troubleshooting

| Symptom | Cause | Fix |
|---------|-------|-----|
| No notifications with the terminal window closed | `system` / `terminal` notifications are delivered by the attached client | Minimize the window instead of closing it. State is still tracked and shows on reattach. |
| A tool installed after herdr started is "not found" | The server keeps the PATH it started with | `herdr server stop`, then `herdr` |
| glow opened from yazi shows a blank screen | Windows quirk with glow as a `block` opener inside herdr (popup and pane). glow alone renders fine. | Press a key (`r`) to repaint. Accepted as a known quirk; could be automated later with `herdr pane send-keys` and a small script. |
| Popup cannot be zoomed | Popups are modal overlays, not panes | Use a `pane` command type and `ctrl+b z` |
| `ctrl+b alt+g` typed `lazygit` into Claude | The command types into the focused pane | Focus a shell pane first |
| Config change has no effect | Server still has the old config | `herdr server reload-config` |

## Notes

- `Shift+Enter` is reported correctly by Windows Terminal on this machine. herdr and yazi docs warn it may not be on some terminals.
- Windows Terminal lacks Kitty graphics, hence `terminal.kitty_graphics = false`.
- The drawn cursor on Windows is steady (non-blinking) by design. Set `ui.host_cursor = "native"` to revert.

## New panes open Windows PowerShell 5.1 instead of PowerShell 7

Symptom: errors in the old `En línea: 1 Carácter: 1 / CategoryInfo` format, and the PowerShell 7 profile (zoxide, etc.) is not loaded.

Cause: PowerShell 7 installed from the Microsoft Store (MSIX) is only reachable through the `WindowsApps` app-execution alias, and herdr's shell auto-detection falls back to `powershell.exe`.

Fix: set the shell explicitly in `config.toml` and open a new pane (existing panes keep their shell):

```toml
[terminal]
default_shell = "pwsh.exe"
```

Check with `$PSVersionTable.PSVersion` inside the pane.
