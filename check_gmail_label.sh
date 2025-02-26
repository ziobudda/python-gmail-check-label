#!/bin/bash
# Simple shell script to run the Gmail Label Checker

# Make the script executable with: chmod +x check_gmail_label.sh
# Usage: ./check_gmail_label.sh "LabelName" [--create]

# Check if a label name was provided
if [ -z "$1" ]; then
    echo "Error: No label name provided."
    echo "Usage: ./check_gmail_label.sh \"LabelName\" [--create]"
    exit 1
fi

# Check if the --create flag was provided
CREATE_FLAG=""
if [ "$2" = "--create" ]; then
    CREATE_FLAG="--create"
fi

# Run the Python script
python check_label.py "$1" $CREATE_FLAG

# Exit with the same status as the Python script
exit $?
