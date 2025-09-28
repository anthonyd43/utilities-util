from enum import Enum

class PaymentMethod(Enum):
    PAYPAL = "paypal"
    BANK_TRANSFER = "bank_transfer"
    VENMO = "venmo"
    CASH = "cash"
    ZELLE = "zelle"

class SplitType(Enum):
    EQUAL = "equal"
    CUSTOM = "custom"
    PERCENTAGE = "percentage"
    USAGE_BASED = "usage_based"