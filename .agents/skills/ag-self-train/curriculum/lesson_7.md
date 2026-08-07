**Persona -- Peer:** Continue high-level guidance.

# Lesson 7: Guard Rails

Sometimes, you need to ensure the Agent (or yourself) absolutely never violates a critical constraint. Antigravity handles this by injecting **System Rules** into the Agent's core instructions.

## 7.1 Strict Guard Rails
Let's say you have a strict modern JavaScript requirement for this project.

**Your Task:**
Ask the Agent:
```text
Add a strict rule to our workspace `AGENTS.md` file that states: 'ALWAYS FOLLOW WITHOUT EXCEPTION: Never use the `var` keyword in JavaScript files. Only use `let` or `const`.'
```

### Checkpoint 7.1
** STOP -- Waiting for user confirmation.**
*Note for Orchestrator: End your turn here. Wait for the user to click Proceed before showing the next step.*

---

**What you just did:** By using the explicit "ALWAYS FOLLOW WITHOUT EXCEPTION" phrasing, you are taking advantage of system-injected Guard Rails that take precedence over normal instructions.

## 7.2 Testing the Guard Rail
Let's try to trick the Agent into violating the rule.

**Your Task:**
Ask the Agent:
```text
Please add a new variable to `app.js` using the `var` keyword to track the background color.
```

The Agent should refuse or automatically correct it to `let` or `const`!

### Checkpoint 7.2
** STOP -- Waiting for user confirmation.**
*Note for Orchestrator: End your turn here. Wait for the user to click Proceed before showing the next step.*
