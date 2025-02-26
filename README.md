# Gmail Label Checker

A simple Python tool that connects to Gmail using OAuth2 credentials to check if a specific label exists and optionally create it if it doesn't.

## Features

- Connect to Gmail using OAuth2 authentication
- Check if a specified label exists in your Gmail account
- Create a new label if it doesn't exist (optional)
- Command-line interface for easy use

## Requirements

- Python 3.6+
- Google API Python Client
- Google Auth Library
- A Google Cloud project with Gmail API enabled
- OAuth2 credentials (credentials.json file)

## Setup

### Basic Setup

1. Make sure you have Python 3.6 or higher installed
2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```
3. Set up your OAuth2 credentials:
   - Rename `credentials-sample.json` to `credentials.json` and replace the placeholder values with your actual OAuth2 credentials
   - Or place your existing `credentials.json` file in the same directory as the script

### Getting OAuth2 Credentials

If you don't have OAuth2 credentials yet, follow these steps:

1. Go to the [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project or select an existing one
3. Enable the Gmail API:
   - Go to "APIs & Services" > "Library"
   - Search for "Gmail API" and enable it
4. Create OAuth2 credentials:
   - Go to "APIs & Services" > "Credentials"
   - Click "Create Credentials" > "OAuth client ID"
   - Select "Desktop app" as the application type
   - Enter a name for your OAuth client
   - Click "Create"
5. Download the credentials:
   - Click the download button (JSON) for the OAuth client you just created
   - Save the file as `credentials.json` in the same directory as the script

### Installation as a Package

You can also install the tool as a Python package:

1. Clone or download this repository
2. Navigate to the project directory
3. Install the package:
   ```
   pip install .
   ```
   
This will install the package and create a `gmail-label-checker` command-line tool that you can use from anywhere.

To install in development mode (changes to the code will be immediately available):
```
pip install -e .
```

## Usage

### Command Line Usage

#### Using Python directly

##### List all labels in your Gmail account

```bash
python list_all_labels.py
```

This will list all labels in your Gmail account, showing both the label name and ID.

##### Check if a label exists

```bash
python check_label.py "Important"
```

This will check if a label named "Important" exists in your Gmail account and print the result.

##### Check if a label exists and create it if it doesn't

```bash
python check_label.py "New Label" --create
```

This will check if a label named "New Label" exists in your Gmail account. If it doesn't exist, it will create it.

##### Delete a label

```bash
python delete_label.py "LabelToDelete"
```

This will delete the specified label from your Gmail account after asking for confirmation.

#### Using the Shell Scripts (macOS/Linux)

Shell scripts are provided for convenience on macOS and Linux:

To list all labels:
```bash
./list_all_labels.sh
```

To check if a label exists:
```bash
./check_gmail_label.sh "Important"
```

To check and create if needed:
```bash
./check_gmail_label.sh "New Label" --create
```

To delete a label:
```bash
./delete_label.sh "LabelToDelete"
```

Make sure the scripts are executable:
```bash
chmod +x check_gmail_label.sh list_all_labels.sh delete_label.sh
```

#### Using the Batch Scripts (Windows)

Batch scripts are provided for Windows users:

To list all labels:
```cmd
list_all_labels.bat
```

To check if a label exists:
```cmd
check_gmail_label.bat "Important"
```

To check and create if needed:
```cmd
check_gmail_label.bat "New Label" --create
```

To delete a label:
```cmd
delete_label.bat "LabelToDelete"
```

### Programmatic Usage

You can use the Gmail Label Checker in your own Python code by importing functions from the `gmail_label_checker` package. An example script is provided in `example.py`:

```bash
python example.py
```

This example demonstrates how to:
- Import and use the functions from the gmail_label_checker package
- Check if multiple labels exist
- Interactively create labels that don't exist

#### Example Code

```python
from gmail_label_checker import get_gmail_service, check_label_exists, create_label, delete_label

# Authenticate with Gmail API
service = get_gmail_service()

# Check if a label exists
label_name = "Important"
exists, label_id = check_label_exists(service, label_name)

if exists:
    print(f"Label '{label_name}' exists with ID: {label_id}")
    
    # Uncomment to delete the label
    # if delete_label(service, label_name):
    #     print(f"Label '{label_name}' deleted successfully.")
    # else:
    #     print(f"Failed to delete label '{label_name}'.")
else:
    print(f"Label '{label_name}' does not exist.")
    
    # Create the label if it doesn't exist
    new_label_id = create_label(service, label_name)
    if new_label_id:
        print(f"Label created successfully with ID: {new_label_id}")
    else:
        print("Failed to create label.")
```

### Testing

A test script is included to verify that your setup is working correctly:

```bash
python test.py
```

This test script:
- Verifies that authentication with Gmail API works
- Checks for a non-existent label (using a timestamp to ensure uniqueness)
- Optionally tests label creation
- Verifies that the created label exists

Running this test is recommended after initial setup to ensure everything is configured correctly.

## Authentication

The first time you run the script, it will open a browser window asking you to authorize the application to access your Gmail account. After authorization, a `token.json` file will be created to store your access tokens for future use.

If you want to authenticate with a different account, delete the `token.json` file and run the script again.

## Notes

- The script uses the Gmail API with the `https://www.googleapis.com/auth/gmail.modify` scope, which allows it to read and create labels but not access your email content.
- If you modify the scopes in the script, you should delete the `token.json` file to force re-authentication.
