@echo off

REM check if Python is installed
where python >nul 2>&1
if %errorlevel% == 0 (
    REM run the Python script
    python main.py
) else (
    REM print an error message
    echo Python is not installed on this system.
)
