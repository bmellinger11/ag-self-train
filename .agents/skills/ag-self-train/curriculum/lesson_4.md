**Persona -- Collaborator:** Work alongside the user. Provide the structural ideas but ask them to fill in the gaps. "What do you think we should do next?"

# Lesson 4: Skills and Commands

Your canvas project is looking great with that strict styling rule! Now let's explore **Custom Skills** and **Slash Commands**. 

## 4.1 What are Skills?
Skills are specialized folders containing a `SKILL.md` file that teach the Agent how to handle complex, specialized tasks. When you mention a concept that a Skill covers, the Agent automatically reads its instructions. 

## 4.2 Creating a Custom Skill
Let's build a skill that generates complementary color palettes for your canvas!

**Your Task:**
Ask the Agent the following:
```text
Please create a new custom skill located at `.agents/skills/color-palette/SKILL.md`. The skill should trigger whenever I mention 'color palette', and its instructions should tell you to generate 3 complementary vibrant HEX colors and apply them randomly to the canvas shapes in `app.js`.
```

### Checkpoint 4.1
** STOP -- Waiting for user confirmation.**
*Note for Orchestrator: End your turn here. Wait for the user to click Proceed before showing the next step.*

---

**What you just did:** You created an executable instruction set that expands the Agent's core capabilities.

## 4.3 Slash Commands
Sometimes you want to explicitly invoke a specific Agent workflow. **Slash Commands** (like `/goal`, `/schedule`, or `/learn`) are native shortcuts you can type into the chat.

## 4.4 Triggering Your Skill
Let's use the `/goal` command to trigger your new skill in a highly focused execution mode.

**Your Task:**
Type the following into the chat:
```text
/goal Apply a new color palette to my canvas shapes.
```

The Agent should detect the trigger, read your `color-palette` skill, and update `app.js` with new complementary colors!

### Checkpoint 4.2
** STOP -- Waiting for user confirmation.**
*Note for Orchestrator: End your turn here. Wait for the user to click Proceed before showing the next step.*
