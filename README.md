# ToDo App

## Local Setup

1. Open a terminal in the project folder:
   - `[path-to-your-progect]`

2. Verify Python is installed:
   - `python --version`

3. Create a virtual environment:
   - `python -m venv .venv`

4. Activate the virtual environment:
   - PowerShell: `& .\.venv\Scripts\Activate.ps1`
   - CMD: `.\.venv\Scripts\activate`
   - Git Bash: `source .venv/Scripts/activate`

5. Install dependencies:
   - `python -m pip install -r requirements.txt`

6. Run the app:
   - `python app.py`

7. Open the app in your browser:
   - `http://127.0.0.1:5000`

## Notes

- If PowerShell blocks script execution, run:
  - `Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass`

- The app uses SQLite and will create `tasks.db` automatically on first run.

## Live Demo

https://todo-app-kjp3.onrender.com

## About
This is my Todo App.

