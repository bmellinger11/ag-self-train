**Persona -- Guide:** Maintain a patient, guiding tone. Explain Planning Mode thoroughly.

# Module 2: Blueprint and Build

In Module 1, you asked the Agent to execute a simple, one-off task. But what happens when you want to build something complex that requires architectural changes across multiple files?

That's where **Planning Mode** comes in.

## 2.1 The Need for Planning
When a task is highly complex, the Agent automatically enters Planning Mode before making any code changes. It researches the codebase, formulates a strategy, and presents an `implementation_plan.md` Artifact for your approval.

You can explicitly force the Agent into Planning Mode for any task by using the `/goal` slash command, or simply by asking it to "create a plan".

## 2.2 Adding Animation
Let's make our boring green rectangle move! We want it to bounce around the canvas edges. This is a bit more complex, so let's use Planning Mode.

**Your Task:**
Type the following prompt into the chat:
> "Please create a plan to make the green rectangle bounce around the canvas. Request my feedback so I can review it before you write the code."

** STOP -- What you just did:** You instructed the Agent to formulate a strategy rather than immediately writing code. The Agent should now present you with an `implementation_plan.md` Artifact outlining the necessary changes to `app.js` to create an HTML animation loop.

## 2.3 Approving the Plan and Tracking Tasks
Read through the implementation plan. If it looks good, click the **Proceed** button in the UI. 

Once approved, the Agent will begin execution. It will automatically generate a `task.md` checklist Artifact so you can track its progress as it modifies your files.

### Checkpoint 2
** STOP -- Waiting for user confirmation.**
*Note for Orchestrator: End your turn here. Wait for the user to run the prompt and say 'continue' before showing the next step.*
