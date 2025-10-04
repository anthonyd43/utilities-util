from src.integrations.gmail import get_creds, get_emails


if __name__ == "__main__":
    creds = get_creds()
    emails = get_emails(creds, subject="bill")
    # print subjects of emails
    for email in emails:
        print(f"Email ID: {email.id}, Subject: {email.subject}, Date: {email.date}, From: {email.sender}, To: {email.recipient}, Has Attachment: {email.has_attachment}")
    print(f"Found {len(emails)} emails with subject 'bill'")
