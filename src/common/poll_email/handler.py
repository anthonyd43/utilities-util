from src.integrations.gmail import get_creds, get_emails

def handler():
    """
    This handler will be called by a cron job hosted in Github Actions every hour to poll for new emails.
    It will use the Gmail API to fetch emails and process them accordingly.
    The emails will be filtered based on predefined patterns from BillEmailPattern models (stored in the database).
    1. Fetch all active BillEmailPattern from the database.
    2. For each pattern, use the Gmail API to search for matching emails.
    3. For each matching email, extract relevant information (e.g., amount, due date) using regex.
    """
    creds = get_creds()
    emails = get_emails(creds, subject="bill")
    # Process the emails as needed
    for email in emails:
        print(f"Email ID: {email.id}, Subject: {email.subject}, Date: {email.date}, From: {email.sender}, To: {email.recipient}, Has Attachment: {email.has_attachment}")
    print(f"Found {len(emails)} emails with subject 'bill'")