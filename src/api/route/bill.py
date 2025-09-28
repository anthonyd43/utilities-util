from fastapi import APIRouter
from src.common.models.bill import Bill, BillEmailPattern

router = APIRouter(
    prefix="/bill",
    tags=["Bills"],
)


@router.get("/", response_model=list[Bill])
async def get_bills():
    # Placeholder implementation
    return []

@router.get("/{bill_id}", response_model=Bill)
async def get_bill(bill_id: int):
    # Placeholder implementation
    return Bill(id=bill_id, amount=100.0, bill_due_date="2024-12-31")

@router.post("/", response_model=Bill)
async def create_bill(bill: Bill):
    # Placeholder implementation
    return bill

@router.get("/email-patterns", response_model=list[BillEmailPattern])
async def get_bill_email_patterns():
    # Placeholder implementation
    return []

@router.post("/email-patterns", response_model=BillEmailPattern)
async def create_bill_email_pattern(pattern: BillEmailPattern):
    # Placeholder implementation
    return pattern

@router.put("/email-patterns/{pattern_id}", response_model=BillEmailPattern)
async def update_bill_email_pattern(pattern_id: int, pattern: BillEmailPattern):
    # Placeholder implementation
    return pattern

@router.delete("/email-patterns/{pattern_id}")
async def delete_bill_email_pattern(pattern_id: int):
    # Placeholder implementation
    return {"detail": "Pattern deleted"}

