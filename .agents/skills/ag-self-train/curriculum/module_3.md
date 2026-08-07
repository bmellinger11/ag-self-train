**Persona -- Guide:** Continue defining concepts clearly. Introduce Customization Roots.

# Module 3: Rules and Context

Your bouncing rectangle looks great! But as your project grows, you'll want the Agent to automatically follow specific conventions without having to remind it every time. 

Antigravity IDE solves this with **Customizations**, specifically the `AGENTS.md` rules file and Knowledge Items (KIs).

## 3.1 Workspace Rules (`AGENTS.md`)
You can define rules that apply to your entire workspace by placing an `AGENTS.md` file inside the `.agents/` Customization Root folder. The Agent will read these rules at the start of every task and adhere to them strictly.

Actually, we already created an `AGENTS.md` file during the curriculum initialization! If you open `.agents/AGENTS.md`, you'll see a rule instructing the Agent not to provide direct solutions.

## 3.2 Defining a New Rule
Let's add a stylistic rule for our Canvas drawings.

**Your Task:**
Open the `.agents/AGENTS.md` file and add the following line to the bottom:
> "- Rule: Whenever you draw a shape on the canvas, always use a vibrant, colorful HEX code (e.g. #FF0055). Never use basic color names like 'red' or 'green'."

** STOP -- What you just did:** You've just extended the Agent's system prompt! Now, any time it interacts with your Canvas project, it will naturally prefer hex codes over basic color names. 

## 3.3 Testing Your Rule
Let's see if the Agent obeys the new rule.

**Your Task:**
Ask the Agent the following:
> "Please add a new bouncing circle to the canvas. Make sure you follow our project rules for styling."

The Agent should draw the circle using a hex code instead of a basic color name, automatically reading your `AGENTS.md` file for context!

### Checkpoint 3
** STOP -- Waiting for user confirmation.**
*Note for Orchestrator: End your turn here. Wait for the user to run the prompt and say 'continue' before showing the next step.*
