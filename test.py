#!/usr/bin/env python3
"""
Test script for Gmail Label Checker.

This script performs a simple test to verify that:
1. Authentication with Gmail API works correctly
2. The label checking functionality works
3. The label creation functionality works (if requested)

Usage:
    python test.py
"""

import os
import sys
import time
from gmail_label_checker import get_gmail_service, check_label_exists, create_label

def run_test():
    """Run a simple test of the Gmail Label Checker functionality."""
    print("=== Gmail Label Checker Test ===")
    
    # Test label name (using timestamp to ensure uniqueness)
    timestamp = int(time.time())
    test_label = f"TestLabel_{timestamp}"
    
    print(f"\n1. Testing authentication...")
    try:
        service = get_gmail_service()
        print("✓ Authentication successful!")
    except Exception as e:
        print(f"✗ Authentication failed: {e}")
        return False
    
    print(f"\n2. Testing label check for a unique label: '{test_label}'")
    try:
        exists, label_id = check_label_exists(service, test_label)
        if exists:
            print(f"! Unexpected: Label '{test_label}' already exists with ID: {label_id}")
            print("  This is unusual since we generated a unique label name with timestamp.")
        else:
            print(f"✓ As expected, label '{test_label}' does not exist.")
    except Exception as e:
        print(f"✗ Label check failed: {e}")
        return False
    
    print(f"\n3. Testing label creation for: '{test_label}'")
    try:
        create_test = input("Do you want to test label creation? (y/n): ")
        if create_test.lower() == 'y':
            new_label_id = create_label(service, test_label)
            if new_label_id:
                print(f"✓ Label created successfully with ID: {new_label_id}")
                
                # Verify the label was created
                print(f"\n4. Verifying label creation...")
                exists, label_id = check_label_exists(service, test_label)
                if exists and label_id == new_label_id:
                    print(f"✓ Label verification successful! Label exists with ID: {label_id}")
                else:
                    print(f"✗ Label verification failed. Label not found or ID mismatch.")
            else:
                print("✗ Failed to create label.")
        else:
            print("- Label creation test skipped.")
    except Exception as e:
        print(f"✗ Label creation test failed: {e}")
        return False
    
    print("\n=== Test Completed Successfully ===")
    return True

if __name__ == "__main__":
    run_test()
