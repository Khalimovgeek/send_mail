from setuptools import setup, find_packages
import webbrowser
import send_mail.authenticater_script.py  # Import authentication module

setup(
    name='mail',
    version='1.0.0',
    packages=find_packages(),
    py_modules=['mail_script'],
    install_requires=[
        'google-api-python-client',
        'google-auth-oauthlib',
        'google-auth-httplib2'
        # Add other dependencies here, if any
    ],
    entry_points={
        'console_scripts': [
            'mail=mail_script:main',  # This maps the command `mail` to the `main` function
        ],
    },
)

GMAIL_API_URL = "https://console.cloud.google.com/apis/library/gmail.googleapis.com"
CREDENTIALS_URL = "https://console.cloud.google.com/apis/credentials"

print("\n✅ Installation successful!")
print("🚀 Next step: Setup Gmail API.")
print("Redirecting to Google API Console...")

# Automatically open the Gmail API page for the user
webbrowser.open(GMAIL_API_URL)

# After enabling, prompt user to create credentials
print("\n🔑 After enabling Gmail API, create OAuth credentials.")
print("Opening Credentials Setup Page...")

# Automatically open credentials creation page
webbrowser.open(CREDENTIALS_URL)

# Check if credentials.json exists
send_mail.auth.check_credentials()
