@echo off
REM Simple batch script to delete a Gmail label on Windows
REM Usage: delete_label.bat "LabelName"

REM Check if a label name was provided
if "%~1"=="" (
    echo Error: No label name provided.
    echo Usage: delete_label.bat "LabelName"
    exit /b 1
)

REM Run the Python script
python delete_label.py "%~1"

REM Exit with the same status as the Python script
exit /b %ERRORLEVEL%
