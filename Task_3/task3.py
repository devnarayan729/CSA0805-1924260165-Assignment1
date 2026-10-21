from decimal import Decimal

BASE_RATE = Decimal("30.00")
FAT_STEP_VALUE = Decimal("0.40")
SNF_STEP_VALUE = Decimal("0.30")
STANDARD_FAT = Decimal("3.5")
STANDARD_SNF = Decimal("8.5")
QUALITY_STEP = Decimal("0.1")
MIN_FAT = Decimal("2.0")
MAX_FAT = Decimal("7.0")

value = 10
print(value, type(value).__name__)
value = "ten"
print(value, type(value).__name__)

litres, fat, snf = Decimal("10"), Decimal("3.5"), Decimal("8.5")
print("Milk measurements:", litres, fat, snf)

left, right = "morning", "evening"
left, right = right, left
print("After swapping:", left, right)

RATE_CARD = {
    "base": BASE_RATE,
    "fat_step": FAT_STEP_VALUE,
    "snf_step": SNF_STEP_VALUE,
}
print("Rate card:", RATE_CARD)
