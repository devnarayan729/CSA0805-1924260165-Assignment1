import math
from decimal import Decimal, ROUND_HALF_UP

BASE_RATE = Decimal("30.00")
FAT_STEP_VALUE = Decimal("0.40")
SNF_STEP_VALUE = Decimal("0.30")
STANDARD_FAT = Decimal("3.5")
STANDARD_SNF = Decimal("8.5")
QUALITY_STEP = Decimal("0.1")


def steps(value, standard):
    difference = Decimal(str(value)) - Decimal(str(standard))
    return int(
        (difference / QUALITY_STEP).quantize(
            Decimal("1"),
            rounding=ROUND_HALF_UP,
        )
    )


def rate_per_litre(fat, snf):
    return (
        BASE_RATE
        + Decimal(steps(fat, STANDARD_FAT)) * FAT_STEP_VALUE
        + Decimal(steps(snf, STANDARD_SNF)) * SNF_STEP_VALUE
    )


print("(4.2 - 3.5) / 0.1 =", (4.2 - 3.5) / 0.1)
print("0.1 + 0.2 == 0.3 =", 0.1 + 0.2 == 0.3)
print("-7 // 2 =", -7 // 2)
print("int(-3.9) =", int(-3.9))
print("math.floor(-3.9) =", math.floor(-3.9))
print("round(2.5) =", round(2.5))
print("round(-2.5) =", round(-2.5))
print("-2 ** 2 =", -2 ** 2)
print("(-2) ** 2 =", (-2) ** 2)
print("2 ** 3 ** 2 =", 2 ** 3 ** 2)

for fat in (4.2, 3.1):
    decimal_steps = steps(fat, STANDARD_FAT)
    int_steps = int((fat - 3.5) / 0.1)
    floor_steps = math.floor((fat - 3.5) / 0.1)
    print(
        f"fat={fat}: nearest={decimal_steps}, "
        f"int rate={BASE_RATE + Decimal(int_steps) * FAT_STEP_VALUE:.2f}, "
        f"floor rate={BASE_RATE + Decimal(floor_steps) * FAT_STEP_VALUE:.2f}, "
        f"nearest rate={BASE_RATE + Decimal(decimal_steps) * FAT_STEP_VALUE:.2f}"
    )

print("Chained range check:", 2.0 <= 3.5 <= 7.0)
print("Boolean validation:", 2.0 <= 3.5 <= 7.0 and 0.0 <= 8.5 <= 20.0)
print("10 L payment:", rate_per_litre(4.2, 8.7) * Decimal("10"))
