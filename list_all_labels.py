#!/usr/bin/env python3
"""
List All Gmail Labels

This script lists all labels in your Gmail account.
It uses OAuth2 authentication with credentials from a credentials.json file.

Usage:
    python list_all_labels.py
"""

from gmail_label_checker import get_gmail_service
from googleapiclient.errors import HttpError

def list_all_labels():
    """List all labels in the user's Gmail account."""
    try:
        # Get the authenticated Gmail service
        print("Authenticating with Gmail...")
        service = get_gmail_service()
        print("Authentication successful!")
        
        # Get all labels in the user's account
        print("\nRetrieving labels...")
        results = service.users().labels().list(userId='me').execute()
        labels = results.get('labels', [])
        
        if not labels:
            print("No labels found in your Gmail account.")
            return
        
        # Print all labels
        print(f"\nFound {len(labels)} labels in your Gmail account:")
        print("-" * 50)
        print(f"{'LABEL NAME':<30} {'LABEL ID':<20}")
        print("-" * 50)
        
        # Sort labels alphabetically by name
        for label in sorted(labels, key=lambda x: x['name'].lower()):
            print(f"{label['name']:<30} {label['id']:<20}")
        
        print("-" * 50)
        
    except HttpError as error:
        print(f"An error occurred: {error}")

if __name__ == '__main__':
    list_all_labels()
