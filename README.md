# maya-breaktime-reminder

This is a lightweight Python script for Autodesk Maya that displays a fun and interactive **Energy Bar UI**. It's designed to help artists take timely breaks by simulating an "energy drain" during work sessions. When your energy gets too low, the script reminds you to pause and refresh yourself!

## ✨ Features

- 🔋 Shows a live **Energy Bar** starting at 100%.
- ⏳ Energy decreases every 1800 seconds while the timer is running.
- 🍵 When energy falls below 10%, it prompts a **break reminder** dialog.
- 🧵 Runs in a background thread without freezing Maya UI.
- 💬 Friendly and cute reminder message to lighten up your day.

## 📂 File

- `main.py`: The main script file to run inside Maya's script editor or shelf.

## 🚀 How to Use

1. Open **Autodesk Maya**.
2. Drag and drop or paste the contents of `main.py` into the **Script Editor** (Python tab).
3. Run the script.
4. A UI window titled **Maya Energy Bar** will appear.
5. Click the **"Let's Go! 🚀"** button to start the energy countdown.
6. When the bar hits low energy, take a well-deserved break! 🧃

## 🛠️ Requirements

- **Autodesk Maya**
- Python (comes pre-installed with Maya)
- No external dependencies

## 📌 Notes

- The script is intended for fun and productivity balance. Feel free to modify the drain speed or break message as per your preferences.
- If the UI is closed, the energy draining stops automatically.

---

Happy animating! 🎨🧘‍♀️
