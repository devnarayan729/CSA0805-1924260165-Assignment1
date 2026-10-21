from decimal import Decimal

BASE_RATE = Decimal("30.00")
FAT_STEP_VALUE = Decimal("0.40")
SNF_STEP_VALUE = Decimal("0.30")

entry = {
    "farmer_id": "F001",
    "litres": Decimal("10.0"),
    "fat": Decimal("3.5"),
    "snf": Decimal("8.5"),
    "shift": "morning"
}

print("Farmer entry:", entry)
print("Base rate:", BASE_RATE)
print("Fat adjustment:", FAT_STEP_VALUE)
print("SNF adjustment:", SNF_STEP_VALUE)
print("Rules: litres > 0 and fat between 2.0% and 7.0%.")