**Persona -- Guide:** Explain everything step-by-step. Define terms on first use. Celebrate small wins. "Let's try…", "Here's what that does…"

# Module 1: Setup and First Contact

Welcome to the Canvas project! In this curriculum, you won't just write code yourself—you'll learn how to direct the **Antigravity IDE Agent** to build it for you. 

By the end of this module, you will have set up a basic HTML Canvas application using the Agent Chat UI, and you'll understand how the Agent presents structured data to you.

## 1.1 The Agent Chat UI
You are already interacting with the Agent (me!) right now. Unlike traditional coding where you type every line, in Antigravity you describe *what* you want, and the Agent autonomously writes the code, creates files, and runs commands in your workspace.

## 1.2 Your First Prompt
Let's get our project scaffolded. We need an `index.html` file and an `app.js` file to hold our canvas logic. 

Instead of creating these manually, ask the Agent to do it!

**Your Task:**
Type the following prompt into the chat and hit Enter:
> "Please create an `index.html` file with a 400x400 `<canvas>` element with id 'myCanvas'. Also create an `app.js` file linked to the HTML that draws a solid green rectangle on the canvas."

*Note: The Agent will generate the files and show you a diff of what was created.*

** STOP -- What you just did:** You successfully delegated a coding task to the Agent! Notice how the Agent didn't just give you code to copy-paste; it actually created the files in your workspace directly.

## 1.3 Understanding Artifacts
When the Agent has a lot of structured information to share—like a complex plan, a markdown table, or a visual diagram—it won't dump it all into the chat stream. Instead, it uses **Artifacts**.

You might have already seen an Artifact when the Agent created the files (perhaps a walkthrough or a checklist). Artifacts are special, rich markdown documents that persist in your project's `.gemini/` brain folder. They keep the chat clean and are easy to review.

### Checkpoint 1
** STOP -- Waiting for user confirmation.**
*Note for Orchestrator: End your turn here. Wait for the user to run the prompt and say 'continue' before showing the next step.*
