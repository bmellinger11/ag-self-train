# Module 1: Getting Started with Canvas

Welcome to the Canvas project! In this module, we will set up our HTML file with a `<canvas>` element and draw a simple rectangle.

````carousel
```html
<!-- Step 1: index.html -->
<!DOCTYPE html>
<html>
<head>
  <title>Canvas Project</title>
</head>
<body>
  <canvas id="myCanvas" width="400" height="400"></canvas>
  <script src="app.js"></script>
</body>
</html>
```
<!-- slide -->
```javascript
// Step 2: app.js
const canvas = document.getElementById('myCanvas');
const ctx = canvas.getContext('2d');
ctx.fillStyle = 'green';
ctx.fillRect(10, 10, 150, 100);
```
````

### Task for the Learner
1. Create `index.html` and copy the code from Step 1.
2. Create `app.js` and copy the code from Step 2.

*Note for AI Orchestrator:* Use the `ask_question` tool to ask the user "Have you completed Step 1 and 2?" before moving to Module 2.
