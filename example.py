#!/usr/bin/env python3
"""
Example script demonstrating how to use the Gmail Label Checker in your own Python code.

This script shows how to:
1. Import and use the functions from the gmail_label_checker package
2. Check if a label exists
3. Create a label if it doesn't exist
4. Delete a label if needed
"""

from gmail_label_checker import get_gmail_service, check_label_exists, create_label, delete_label

def main():
    # Example label names
    labels_to_check = ["Important", "Work", "Personal", "CustomLabel123"]
    
    # Get the Gmail service
    print("Authenticating with Gmail...")
    service = get_gmail_service()
    print("Authentication successful!")
    
    # Check if each label exists
    print("\nChecking labels:")
    for label_name in labels_to_check:
        exists, label_id = check_label_exists(service, label_name)
        
        if exists:
            print(f"✓ Label '{label_name}' exists with ID: {label_id}")
            
            # Ask if user wants to delete the label
            delete_it = input(f"Do you want to delete the label '{label_name}'? (y/n): ")
            if delete_it.lower() == 'y':
                if delete_label(service, label_name):
                    print(f"  ✓ Label '{label_name}' deleted successfully.")
                else:
                    print(f"  ✗ Failed to delete label '{label_name}'.")
        else:
            print(f"✗ Label '{label_name}' does not exist.")
            
            # Ask if user wants to create the label
            create_it = input(f"Do you want to create the label '{label_name}'? (y/n): ")
            if create_it.lower() == 'y':
                new_label_id = create_label(service, label_name)
                if new_label_id:
                    print(f"  ✓ Label created successfully with ID: {new_label_id}")
                    
                    # Ask if user wants to delete the newly created label
                    delete_it = input(f"Do you want to delete the newly created label '{label_name}'? (y/n): ")
                    if delete_it.lower() == 'y':
                        if delete_label(service, label_name):
                            print(f"  ✓ Label '{label_name}' deleted successfully.")
                        else:
                            print(f"  ✗ Failed to delete label '{label_name}'.")
                else:
                    print("  ✗ Failed to create label.")

if __name__ == "__main__":
    main()
