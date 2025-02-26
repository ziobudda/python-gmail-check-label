#!/usr/bin/env python3
"""
Core functionality for Gmail Label Checker.

This module provides functions to:
1. Authenticate with Gmail API using OAuth2
2. Check if a label exists
3. Create a new label
"""

import os
import json
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the token.json file.
# Using the modify scope to allow both reading and creating labels
SCOPES = ['https://www.googleapis.com/auth/gmail.modify']

def get_gmail_service():
    """
    Authenticate and create a Gmail API service.
    
    Returns:
        A Gmail API service object if authentication is successful.
    """
    creds = None
    # The token.json file stores the user's access and refresh tokens
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_info(
            info=json.loads(open('token.json').read()), scopes=SCOPES)
    
    # If there are no valid credentials, let the user log in
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    
    # Build and return the Gmail service
    return build('gmail', 'v1', credentials=creds)

def check_label_exists(service, label_name):
    """
    Check if a label with the given name exists.
    
    Args:
        service: Authenticated Gmail API service instance.
        label_name: Name of the label to check.
        
    Returns:
        A tuple (exists, label_id) where exists is a boolean indicating if the label exists,
        and label_id is the ID of the label if it exists, otherwise None.
    """
    try:
        # Get all labels in the user's account
        results = service.users().labels().list(userId='me').execute()
        labels = results.get('labels', [])
        
        if not labels:
            print("No labels found.")
            return False, None
        
        # Check if the specified label exists
        for label in labels:
            if label['name'].lower() == label_name.lower():
                return True, label['id']
        
        return False, None
    
    except HttpError as error:
        print(f"An error occurred: {error}")
        return False, None

def create_label(service, label_name):
    """
    Create a new label with the given name.
    
    Args:
        service: Authenticated Gmail API service instance.
        label_name: Name of the label to create.
        
    Returns:
        The ID of the newly created label if successful, otherwise None.
    """
    try:
        # Create label
        new_label = {
            'name': label_name,
            'labelListVisibility': 'labelShow',
            'messageListVisibility': 'show'
        }
        
        created_label = service.users().labels().create(
            userId='me', body=new_label).execute()
        
        return created_label['id']
    
    except HttpError as error:
        print(f"An error occurred while creating the label: {error}")
        return None

def delete_label(service, label_name):
    """
    Delete a label with the given name.
    
    Args:
        service: Authenticated Gmail API service instance.
        label_name: Name of the label to delete.
        
    Returns:
        True if the label was deleted successfully, False otherwise.
    """
    try:
        # First check if the label exists
        exists, label_id = check_label_exists(service, label_name)
        
        if not exists:
            print(f"Label '{label_name}' does not exist, nothing to delete.")
            return False
        
        # Delete the label
        service.users().labels().delete(userId='me', id=label_id).execute()
        return True
    
    except HttpError as error:
        print(f"An error occurred while deleting the label: {error}")
        return False
