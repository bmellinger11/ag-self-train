**Persona -- Launcher:** Give high-level objectives. Intervene only if they deviate. "Try to orchestrate this..."

# Lesson 8: Subagents

Up to this point, you've been talking to the primary Agent. But Antigravity has the ability to spawn **Subagents** to perform specialized tasks in parallel, specifically the `browser_subagent`.

## 8.1 Spawning a Local Server
To use the browser subagent effectively on our Canvas project, we first need to serve it locally.

**Your Task:**
Ask the Agent:
```text
Please use `manage_task` to spin up a quick Python `http.server` in the background on port 8000.
```

### Checkpoint 8.1
** STOP -- Waiting for user confirmation.**
*Note for Orchestrator: End your turn here. Wait for the user to click Proceed before showing the next step.*

---

## 8.2 Using the Browser Subagent
Now let's orchestrate a subagent!

**Your Task:**
Ask the Agent:
```text
Use the `browser_subagent` to navigate to `http://localhost:8000`. Watch the canvas and report back exactly what shapes and colors you see animating.
```

### Checkpoint 8.2
** STOP -- Waiting for user confirmation.**
*Note for Orchestrator: End your turn here. Wait for the user to click Proceed before showing the next step.*

---

**What you just did:** You delegated a complex visual verification task to a specialized browser-controlling subagent, which then reported back to the main Agent!

## 8.3 Disabling Subagents
Sometimes you explicitly *don't* want the Agent spinning up browser sessions or other subagents without your permission. 

**Your Task:**
Add a standing rule to your `.agents/AGENTS.md` file:
```text
- Rule: Do not use the `browser_subagent` without explicit permission.
```

You can test this by asking the Agent to check a website. It should ask for your permission first!

### Checkpoint 8.3
** STOP -- Waiting for user confirmation.**
*Note for Orchestrator: End your turn here. Wait for the user to click Proceed before showing the next step.*
