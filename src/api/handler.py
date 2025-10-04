from fastapi import FastAPI
from src.api.route import(
    bill,
    email
)

app = FastAPI(
    title="Utilities API",
)

app.include_router(bill.router)
app.include_router(email.router)
