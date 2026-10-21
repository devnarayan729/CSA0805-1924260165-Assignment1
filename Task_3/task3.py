from decimal import Decimal

BASE_RATE = Decimal("30.00")
FAT_STEP_VALUE = Decimal("0.40")
SNF_STEP_VALUE = Decimal("0.30")

value = 10
print(value, type(value))

value = "ten"
print(value, type(value))

litres, fat = 10, 3.5
print("Litres:", litres, "Fat:", fat)

a, b = "left", "right"
a, b = b, a
print("After swapping:", a, b)

RATE_CARD = {
    "base": BASE_RATE,
    "fat": FAT_STEP_VALUE,
    "snf": SNF_STEP_VALUE
}

print(RATE_CARD)