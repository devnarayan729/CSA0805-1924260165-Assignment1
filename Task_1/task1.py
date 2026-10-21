from decimal import Decimal

BASE_RATE = Decimal("30.00")
STANDARD_FAT = Decimal("3.5")
STANDARD_SNF = Decimal("8.5")
FAT_STEP_VALUE = Decimal("0.40")
SNF_STEP_VALUE = Decimal("0.30")
QUALITY_STEP = Decimal("0.1")
MIN_FAT = Decimal("2.0")
MAX_FAT = Decimal("7.0")
MIN_SNF = Decimal("0.0")
MAX_SNF = Decimal("20.0")

entry = {
    "farmer_id": "F001",
    "litres": Decimal("10.0"),
    "fat": Decimal("3.5"),
    "snf": Decimal("8.5"),
    "shift": "morning",
}

print("Inputs:", ", ".join(entry))
print("Types:", {name: type(value).__name__ for name, value in entry.items()})
print("Rate-card constants:", BASE_RATE, FAT_STEP_VALUE, SNF_STEP_VALUE)
print("Validation limits:", MIN_FAT, MAX_FAT, MIN_SNF, MAX_SNF)
print("Example entry:", entry)
