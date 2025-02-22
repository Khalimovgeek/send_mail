import os
import pickle
import webbrowser
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# Define the Gmail API scope
SCOPES = ['https://www.googleapis.com/auth/gmail.send']
TOKEN_FILE = 'token.pickle'
CREDENTIALS_FILE = 'credentials.json'
API_SETUP_URL = "https://console.cloud.google.com/apis/credentials"

def check_credentials():
    """Check if credentials.json exists, if not, prompt the user to set up Gmail API."""
    if not os.path.exists(CREDENTIALS_FILE):
        print("\n🚨 Gmail API credentials not found!")
        print("Follow these steps to enable the Gmail API:\n")
        print("1️⃣ Open: ", API_SETUP_URL)
        print("2️⃣ Click 'Create Credentials' > 'OAuth client ID' > Select 'Desktop App'")
        print("3️⃣ Download and rename it as 'credentials.json'.")
        print("4️⃣ Run this script again.\n")
        
        # Automatically open the API setup page
        webbrowser.open(API_SETUP_URL)
        return False
    return True

def authenticate():
    """Authenticate and get OAuth credentials."""
    creds = None

    # Load existing token if available
    if os.path.exists(TOKEN_FILE):
        with open(TOKEN_FILE, 'rb') as token:
            creds = pickle.load(token)

    # If credentials are not valid, authenticate
    if not creds or not creds.valid:
        try:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(CREDENTIALS_FILE, SCOPES)
                creds = flow.run_local_server(port=0)

            # Save the new token
            with open(TOKEN_FILE, 'wb') as token:
                pickle.dump(creds, token)

            print("✅ Authentication successful! Token saved.")
        except Exception as e:
            print(f"❌ Authentication failed: {e}")
            print("Please check your credentials and try again.")

    return creds

if __name__ == "__main__":
    if check_credentials():
        authenticate()
