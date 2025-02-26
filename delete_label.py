#!/usr/bin/env python3
"""
Delete Gmail Label

This script deletes a specified Gmail label from your account.
It uses OAuth2 authentication with credentials from a credentials.json file.

Usage:
    python delete_label.py "LabelName"
"""

import argparse
from gmail_label_checker import get_gmail_service, delete_label

def main():
    """Main function to delete a Gmail label."""
    # Parse command line arguments
    parser = argparse.ArgumentParser(description='Delete a Gmail label.')
    parser.add_argument('label_name', type=str, help='Name of the label to delete')
    args = parser.parse_args()
    
    # Confirm deletion
    confirm = input(f"Are you sure you want to delete the label '{args.label_name}'? (y/n): ")
    if confirm.lower() != 'y':
        print("Deletion cancelled.")
        return
    
    # Get the authenticated Gmail service
    service = get_gmail_service()
    
    # Delete the label
    if delete_label(service, args.label_name):
        print(f"Label '{args.label_name}' deleted successfully.")
    else:
        print(f"Failed to delete label '{args.label_name}'.")

if __name__ == '__main__':
    main()
