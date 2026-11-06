# Concepts

## Server and client

| Part | Role |
|------|------|
| Server | Owns panes and processes. Keeps running in the background. |
| Client | The UI you see. Detaching (`ctrl+b q`) closes it without stopping anything. |

Bare `herdr` starts the server if needed, or attaches to it. There is no `herdr server start`. `herdr server stop` stops everything.

## Hierarchy

```
session
└── workspace   one per project
    └── tab     a full view
        └── pane    a real terminal, splittable
            └── agent   a process herdr recognizes (e.g. Claude Code)
```

## Agent states

| State | Meaning |
|-------|---------|
| working | The agent is running |
| blocked | Needs your input |
| done | Finished, you have not seen it yet |
| idle | Finished, you have seen it |
| unknown | Not recognized |

## Persistence

| Situation | What survives |
|-----------|---------------|
| Detach / close client (server running) | Everything. Processes never stop. |
| Server or PC restart | Layout, labels and working directories are restored. Processes are lost. |
| Server or PC restart, Claude Code | Conversations are resumed via the integration (`claude --resume <id>`). |
| Server or PC restart, pane screen content | Restored only with `experimental.pane_history = true`. |

## Modes

| Mode | How to enter |
|------|--------------|
| terminal | Default: keys go to the pane |
| prefix | `ctrl+b` |
| navigate | Keyboard navigation between panes and workspaces |
