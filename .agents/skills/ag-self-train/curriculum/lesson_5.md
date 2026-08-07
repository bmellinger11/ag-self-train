**Persona -- Collaborator:** Keep guiding gently. Focus on the value of background automation.

# Lesson 5: Background Observation

So far, you've been telling the Agent exactly what to do. But Antigravity IDE allows the Agent to act independently in the background using **Scheduled Tasks**.

## 5.1 The `/schedule` Command
The `/schedule` command allows you to set up recurring cron jobs or one-shot timers that run silently in the background, notifying the Agent only when necessary.

## 5.2 Creating a One-Shot Timer
Let's set up a background timer. Since running terminal commands in the background requires your explicit permission (as you saw!), we'll just set up a simple timer that tells the Agent to stretch its legs!

**Your Task:**
Ask the Agent to do the following in the chat:
```text
Use the `/schedule` command to set a 60-second one-shot timer (`DurationSeconds`). The prompt should be: 'Time to stretch your legs! Tell the user a quick coding joke.'
```

### Checkpoint 5.1
** STOP -- Waiting for user confirmation.**
*Note for Orchestrator: End your turn here. Wait for the user to click Proceed before showing the next step.*

---

**What you just did:** You spawned an autonomous background process! When it fires in 60 seconds, the Agent will wake up and respond dynamically.

## 5.3 Managing Tasks
You can manage all your background processes using the Agent's `manage_task` capabilities. 

**Your Task:**
Ask the Agent:
```text
List all my running background tasks.
```

You should see your new timer task running smoothly.

### Checkpoint 5.2
** STOP -- Waiting for user confirmation.**
*Note for Orchestrator: End your turn here. Wait for the user to click Proceed before showing the next step.*
