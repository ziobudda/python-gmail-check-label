#!/usr/bin/env python3
"""
Gmail Label Checker

This script checks if a specified Gmail label exists in the user's account.
It uses OAuth2 authentication with credentials from a credentials.json file.

Usage:
    python check_label.py "LabelName"
    python check_label.py "LabelName" --create
"""

import argparse
from gmail_label_checker import get_gmail_service, check_label_exists, create_label

def main():
    """Main function to check if a Gmail label exists."""
    # Parse command line arguments
    parser = argparse.ArgumentParser(description='Check if a Gmail label exists.')
    parser.add_argument('label_name', type=str, help='Name of the label to check')
    parser.add_argument('--create', action='store_true', help='Create the label if it does not exist')
    args = parser.parse_args()
    
    # Get the authenticated Gmail service
    service = get_gmail_service()
    
    # Check if the label exists
    exists, label_id = check_label_exists(service, args.label_name)
    
    # Print the result
    if exists:
        print(f"Label '{args.label_name}' exists with ID: {label_id}")
    else:
        print(f"Label '{args.label_name}' does not exist.")
        
        if args.create:
            print(f"Creating label '{args.label_name}'...")
            new_label_id = create_label(service, args.label_name)
            if new_label_id:
                print(f"Label created successfully with ID: {new_label_id}")
            else:
                print("Failed to create label.")

if __name__ == '__main__':
    import json  # Import here to avoid potential circular imports
    main()
