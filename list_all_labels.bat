@echo off
REM Simple batch script to list all Gmail labels on Windows
REM Usage: list_all_labels.bat

REM Run the Python script
python list_all_labels.py

REM Exit with the same status as the Python script
exit /b %ERRORLEVEL%
