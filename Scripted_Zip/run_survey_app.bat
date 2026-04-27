@echo off
REM Activate your virtual environment if needed
REM call .venv\Scripts\activate

REM Start Flask backend in a new window
start cmd /k "python app.py"

REM Wait a few seconds for Flask to start
timeout /t 3

REM Start a simple HTTP server for the frontend in a new window
start cmd /k "python -m http.server 8000"

REM Open the UI in your default browser
start http://localhost:8000/ScriptedUI.html