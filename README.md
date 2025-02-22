# send_mail

## Overview
`send_mail` is a Python package that allows you to send emails using the Gmail API via the command line. It supports multiple recipients, attachments, and secure authentication.

## Installation
To install `send_mail`, use the following command:

```sh
pip install .
```

After installation, the setup script will guide you through enabling the Gmail API and setting up authentication.

## Setup Gmail API
Since `send_mail` uses the Gmail API, you need to enable it and set up authentication.

### Step 1: Enable the Gmail API
1. Click [this link](https://console.cloud.google.com/apis/library/gmail.googleapis.com) to open the Google Cloud API Library.
2. Click **Enable** to activate the Gmail API for your Google account.

### Step 2: Create OAuth 2.0 Credentials
1. Click [this link](https://console.cloud.google.com/apis/credentials) to open the Credentials page.
2. Click **Create Credentials** > **OAuth client ID**.
3. Choose **Desktop App** as the application type.
4. Click **Create**, then download the JSON file.
5. Rename the file to `credentials.json` and place it in the same directory as `send_mail`.

### Step 3: Authenticate
Run the following command to authenticate with Google:

```sh
python -m send_mail.auth
```

This will open a browser window to grant access. After authentication, a `token.pickle` file will be created for future access.

## Usage
Once setup is complete, you can use `send_mail` to send emails via the command line.

### Send an Email
Run the script using:

```sh
python -m send_mail.mail
```

You'll be prompted to enter:
- Your email address
- Recipient(s) (separate multiple emails with commas)
- Subject
- Message body (use `\n` for line breaks)
- Optional attachments (separate multiple file paths with commas)

The email will be sent via your Gmail account.

## Features
- Send emails via the Gmail API
- Multiple recipients
- Support for attachments with error handling
- Secure authentication using OAuth 2.0
- Automated setup process
- Improved error messages and logging

## Troubleshooting
If you encounter issues:
- Ensure `credentials.json` is in the correct directory.
- Re-authenticate by deleting `token.pickle` and running `python -m send_mail.auth` again.
- Check your Google account settings for security restrictions.
- Verify file paths for attachments to avoid errors.

## License
This project is licensed under the MIT License.
