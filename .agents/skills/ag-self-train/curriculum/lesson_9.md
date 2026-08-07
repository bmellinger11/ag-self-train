**Persona -- Launcher:** "Implement this tracking..."

# Lesson 9: Tasks & TDD

We saw `manage_task` briefly when setting up the server, but let's dive into using it for long-running processes like testing.

## 9.1 Background Testing
**Your Task:**
Ask the Agent:
```text
Please write a mock python script `test_canvas.py` that simulates running a 30-second test suite on the collision logic. Then, use `manage_task` to execute it in the background.
```

### Checkpoint 9.1
** STOP -- Waiting for user confirmation.**
*Note for Orchestrator: End your turn here. Wait for the user to click Proceed before showing the next step.*

---

## 9.2 Checking Status
While the task is running in the background, you can still use the chat! 

**Your Task:**
Ask the Agent to check the status of the background task and generate a `task.md` checklist artifact summarizing the passing tests once it's done.

### Checkpoint 9.2
** STOP -- Waiting for user confirmation.**
*Note for Orchestrator: End your turn here. Wait for the user to click Proceed before showing the next step.*
