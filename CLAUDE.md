# herdr-windows-setup

Documentation and config for a herdr setup on native Windows 11 with Windows Terminal.

## Guiding rule (non-negotiable)

Stability on native Windows comes first. Only propose or add tools, settings and features that are:

1. Documented as supported on native Windows (not WSL-only, not preview, not experimental, not best-effort).
2. Verified on this machine before being committed.
3. Free of Unix assumptions (`sh`, `bash`, `$EDITOR`, Unix-only paths).

Do not suggest herdr gallery plugins, layouts or mods. Prefer herdr built-ins and single-binary native tools. When something is not stable on Windows, say so and stop; do not work around it with scripts.

See `docs/decisions.md` (decision 0) for the rationale and the full list of accepted exceptions.

## Conventions

- Docs, comments and commit messages in English. Conventional commits. No AI attribution lines.
- `config/` mirrors the live files. Validate with `herdr server reload-config` (no diagnostics) before updating a copy here.
- Paths in docs use `%APPDATA%`, `%LOCALAPPDATA%`, `%USERPROFILE%`, never a literal user folder.
- Sources of truth: `herdr --default-config` and the official docs for herdr 0.9.5. Verify against them; do not rely on memory.
