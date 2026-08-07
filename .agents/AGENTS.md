# Antigravity Self-Train Environment

This workspace contains an adaptive learning curriculum for Antigravity IDE users.

- Do not provide direct solutions to the learner unless they are in the 'Guide' persona and need a direct code snippet.
- Adhere to the personas defined in `skills/ag-self-train/SKILL.md`.
- Rule: Whenever you successfully complete a task requested by the user while they are progressing through the self-train curriculum (check `learner_profile.json`), you must automatically generate a `lesson_checkpoint.md` artifact with `RequestFeedback: true` at the very end of your response. This ensures the user has a Proceed button to advance to the next step of the lesson.