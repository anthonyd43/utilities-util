from pydantic import BaseModel
from src.common.models.payment import PaymentMethod

class Housemate(BaseModel):
    id: int
    name: str
    email: str | None = None
    phone: str | None = None
    payment_method: PaymentMethod | None = None