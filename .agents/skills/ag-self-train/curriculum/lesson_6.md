**Persona -- Peer:** Provide high-level suggestions. Best practices focus. "You might want to package this up..."

# Lesson 6: Plugins

Your `.agents/` folder is getting a bit crowded with rules and skills. When you want to share a cohesive set of Customizations with a team, you should group them into a **Plugin**.

## 6.1 Creating a Plugin
A Plugin is simply a directory containing a `plugin.json` configuration file, along with nested `skills/` and `agents/` directories. 

**Your Task:**
Let's package your canvas rules and the color palette skill. Ask the Agent:
```text
Create a new directory at `.agents/plugins/canvas-tools`. Inside it, create a `plugin.json` file defining a plugin named 'Canvas Tools'. Then, move the `color-palette` skill into this plugin's `skills/` directory, and move the rule from `AGENTS.md` into this plugin's `AGENTS.md` file.
```

### Checkpoint 6.1
** STOP -- Waiting for user confirmation.**
*Note for Orchestrator: End your turn here. Wait for the user to click Proceed before showing the next step.*

---

**What you just did:** You modularized your customizations! Now you can easily share `canvas-tools` with other developers.

## 6.2 Verifying the Plugin
Antigravity automatically discovers plugins in the customization root.

**Your Task:**
Ask the Agent:
```text
Is the Canvas Tools plugin loaded and active? Read the plugin.json to confirm.
```

### Checkpoint 6.2
** STOP -- Waiting for user confirmation.**
*Note for Orchestrator: End your turn here. Wait for the user to click Proceed before showing the next step.*
