from googleapiclient.discovery import build
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
import os
import base64
import pickle

def create_message(sender, receiver, subject, message_text, paths=None):
    """Create an email message with optional attachments."""
    message = MIMEMultipart()
    message['to'] = receiver
    message['from'] = sender
    message['subject'] = subject
    message.attach(MIMEText(message_text, 'plain'))
    
    # Attach files if provided
    if paths:
        for path in paths:
            try:
                with open(path, 'rb') as file:
                    attachment = MIMEApplication(file.read(), name=os.path.basename(path))
                    attachment['Content-Disposition'] = f'attachment; filename="{os.path.basename(path)}"'
                    message.attach(attachment)
            except FileNotFoundError:
                print(f"❌ File not found: {path}")
            except Exception as e:
                print(f"⚠️ Error attaching file {path}: {e}")
    
    raw_message = base64.urlsafe_b64encode(message.as_bytes()).decode()
    return {'raw': raw_message}

def send_email(service, user_id, message):
    """Send an email via Gmail API."""
    try:
        sent_message = service.users().messages().send(userId=user_id, body=message).execute()
        print(f"✅ Message sent! Message ID: {sent_message['id']}")
    except Exception as error:
        print(f"❌ An error occurred: {error}")

def main():
    """Main function to send an email."""
    sender = input("Enter your email address: ")
    rec_temp = input("Enter the recipients (separate emails with commas): ")
    receivers = rec_temp.split(',')
    subject = input("Enter the subject: ")
    body = input("Enter the message body (use '\\n' for line breaks): ").replace("\\n", "\n")
    
    attachments = input("Any attachments? (y/n): ").strip().lower()
    paths = None
    if attachments == "y":
        paths_input = input("Enter file paths, separated by commas: ")
        paths = [path.strip() for path in paths_input.split(',')]
    
    # Load credentials
    try:
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    except FileNotFoundError:
        print("❌ Credential file not found. Please authenticate your application.")
        return
    
    service = build('gmail', 'v1', credentials=creds)
    
    for receiver in receivers:
        email_message = create_message(sender, receiver.strip(), subject, body, paths)
        send_email(service, "me", email_message)
    
    print("🎉 All emails sent successfully!")

if __name__ == '__main__':
    main()
