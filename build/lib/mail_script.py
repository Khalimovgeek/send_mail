from googleapiclient.discovery import build
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
import os
import base64
import pickle


def create_message(sender, receiver, subject, message_text, paths=None):
    # Create a MIME message
    message = MIMEMultipart()
    message['to'] = receiver
    message['from'] = sender
    message['subject'] = subject

    # Attach the email body
    message.attach(MIMEText(message_text, 'plain'))

    # Attach files if provided
    if paths:
        for path in paths:
            with open(path, 'rb') as file:
                attachment = MIMEApplication(file.read(), name=os.path.basename(path))
                attachment['Content-Disposition'] = f'attachment; filename="{os.path.basename(path)}"'
                message.attach(attachment)

    # Encode the message
    raw_message = base64.urlsafe_b64encode(message.as_bytes()).decode()
    return {'raw': raw_message}

def send_email(service, user_id, message):
    try:
        sent_message = service.users().messages().send(userId=user_id, body=message).execute()
        print(f"Message sent! Message ID: {sent_message['id']}")
    except Exception as error:
        print(f"An error occurred: {error}")

def main():
    while True:
        sender = input("Enter your email address: ")
        rec_temp = input("Enter the recipients (separate emails with commas): ")
        receivers = rec_temp.split(',')  # Split into a list of email addresses
        subject = input("Enter the subject: ")
        body = input("Enter the message body (use '\\n' for line breaks):")
        body = body.replace("\\n", "\n")
        # Handle attachments
        attachments = input("Any attachments (y/n)? ").lower()
        paths = None
        if attachments == "y":
            paths_input = input("Please specify the file paths, separated by commas: ")
            paths = paths_input.split(',')  # Split into a list of file paths

        # Load credentials
        try:
            with open('token.pickle', 'rb') as token:
                creds = pickle.load(token)
        except FileNotFoundError:
            print("Credential file not found. Please authenticate your application.")
            return

        # Build the Gmail API service
        service = build('gmail', 'v1', credentials=creds)

        # Send emails to all recipients
        for receiver in receivers:
            email_message = create_message(sender, receiver.strip(), subject, body, paths)
            send_email(service, "me", email_message)

        continue_choice = input("Do you want to send another email? (y/n): ").lower()
        if continue_choice != 'y':
            print("Exiting the program. Goodbye!")
            break
        

if __name__ == '__main__':
    main()
