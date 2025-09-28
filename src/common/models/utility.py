from pydantic import BaseModel
from enum import Enum


class UTILITY_TYPE(Enum):
    ELECTRICITY = "electricity"
    WATER = "water"
    INTERNET = "internet"
    GAS = "gas"
    RENT = "rent"
    OTHER = "other"

class Utility(BaseModel):
    id: int
    name: str
    description: str | None = None
    default_price: float | None = None
    is_recurring: bool = True
    is_metered: bool = False
    is_active: bool = True