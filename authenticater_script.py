from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import pickle
import os

# Define the Gmail API scope
SCOPES = ['https://www.googleapis.com/auth/gmail.send']

def authenticate():
    creds = None
    token_file = 'token.pickle'

    # Check if the token already exists
    if os.path.exists(token_file):
        with open(token_file, 'rb') as token:
            creds = pickle.load(token)

    # If no valid credentials, authenticate the user
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)

        # Save the token for future use
        with open(token_file, 'wb') as token:
            pickle.dump(creds, token)

    return creds

# Authenticate and save the token
authenticate()
