#!/bin/bash
# Simple shell script to delete a Gmail label

# Make the script executable with: chmod +x delete_label.sh
# Usage: ./delete_label.sh "LabelName"

# Check if a label name was provided
if [ -z "$1" ]; then
    echo "Error: No label name provided."
    echo "Usage: ./delete_label.sh \"LabelName\""
    exit 1
fi

# Run the Python script
python delete_label.py "$1"

# Exit with the same status as the Python script
exit $?
