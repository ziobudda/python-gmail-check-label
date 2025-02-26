@echo off
REM Simple batch script to run the Gmail Label Checker on Windows
REM Usage: check_gmail_label.bat "LabelName" [--create]

REM Check if a label name was provided
if "%~1"=="" (
    echo Error: No label name provided.
    echo Usage: check_gmail_label.bat "LabelName" [--create]
    exit /b 1
)

REM Check if the --create flag was provided
set CREATE_FLAG=
if "%~2"=="--create" (
    set CREATE_FLAG=--create
)

REM Run the Python script
python check_label.py "%~1" %CREATE_FLAG%

REM Exit with the same status as the Python script
exit /b %ERRORLEVEL%
