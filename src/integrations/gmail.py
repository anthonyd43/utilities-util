import os.path
import os
import pickle
from pathlib import Path
from src.common.models.email import Email
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/gmail.readonly"]


def get_creds():
  creds = None
  # The file token.json stores the user's access and refresh tokens, and is
  # created automatically when the authorization flow completes for the first
  # time.
  if os.path.exists("token.json"):
    creds = Credentials.from_authorized_user_file("token.json", SCOPES)
  # If there are no (valid) credentials available, let the user log in.
  if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
      creds.refresh(Request())
    else:
      flow = InstalledAppFlow.from_client_secrets_file(
          "credentials.json", SCOPES
      )
      creds = flow.run_local_server(port=0)
    # Save the credentials for the next run
    with open("token.json", "w") as token:
      token.write(creds.to_json())
  return creds


def get_labels(creds = None):
  """Shows basic usage of the Gmail API.
  Lists the user's Gmail labels.
  """
  try:
    # Call the Gmail API
    service = build("gmail", "v1", credentials=creds)
    results = service.users().labels().list(userId="me").execute()
    labels = results.get("labels", [])

    if not labels:
      print("No labels found.")
      return
    print("Labels:")
    for label in labels:
      print(label["name"])

  except HttpError as error:
    # TODO(developer) - Handle errors from gmail API.
    print(f"An error occurred: {error}")

def parse_sender(sender: str) -> str:
    if "<" in sender and ">" in sender:
        return sender.split("<")[1].split(">")[0]
    return sender

def get_emails(
    creds = None,
    subject: str | None = None,
    from_email: str | None = None,
    to_email: str | None = None,
    has_attachment: bool = False,
    max_results: int = 10,
) -> list[Email]:
    try:
        service = build("gmail", "v1", credentials=creds)
        query_parts = []
        if subject:
            query_parts.append(f"subject:{subject}")
        if from_email:
            query_parts.append(f"from:{from_email}")
        if to_email:
            query_parts.append(f"to:{to_email}")
        if has_attachment:
            query_parts.append("has:attachment")
        query = " ".join(query_parts) if query_parts else None

        results = service.users().messages().list(
            userId="me", q=query, maxResults=max_results
        ).execute()
        messages = results.get("messages", [])

        if not messages:
            print("No messages found.")
            return []
        
        email_data = []
        for message in messages:
            msg = service.users().messages().get(userId="me", id=message["id"]).execute()
            sender = parse_sender(next((h["value"] for h in msg["payload"]["headers"] if h["name"] == "From"), "No Sender"))

            email = Email(
                id=msg["id"],
                subject=next((h["value"] for h in msg["payload"]["headers"] if h["name"] == "Subject"), "No Subject"),
                date=next((h["value"] for h in msg["payload"]["headers"] if h["name"] == "Date"), "No Date"),
                sender=sender,
                recipient=next((h["value"] for h in msg["payload"]["headers"] if h["name"] == "To"), "No Recipient"),
                body=msg.get("snippet", "No Body"),
                has_attachment="attachments" in msg
            )
            email_data.append(email)

        return email_data

    except HttpError as error:
        # TODO(developer) - Handle errors from gmail API.
        print(f"An error occurred: {error}")

if __name__ == "__main__":
    creds = get_creds()
    emails = get_emails(creds, subject="bill")
    # print subjects of emails
    for email in emails:
        print(f"Email ID: {email.id}, Subject: {email.subject}, Date: {email.date}, From: {email.sender}, To: {email.recipient}, Has Attachment: {email.has_attachment}")
    print(f"Found {len(emails)} emails with subject 'bill'")
    
