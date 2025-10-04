from pydantic import BaseModel
from src.common.models.payment import SplitType

class CreateBillEmailPattern(BaseModel):
    utility_id: str
    pattern: str
    description: str | None = None
    is_active: bool = True

class BillFilterRule(BaseModel):
    id: int
    utility_id: str
    subject_key_word: str
    description: str | None = None
    is_active: bool = True 

class Bill(BaseModel):
    id: int
    amount: float
    usage_start_date: str | None = None
    usage_end_date: str | None = None
    bill_due_date: str
    paid_date: str | None = None
    paid_by: int | None = None  # Housemate ID
    description: str | None = None
    is_paid: bool = False
    split_type: SplitType = SplitType.EQUAL
    active: bool = True
    