from pydantic import BaseModel

class Email(BaseModel):
    id: str
    subject: str | None = None
    date: str | None = None
    sender: str | None = None
    recipient: str | None = None
    body: str | None = None
    has_attachment: bool = False