from decimal import Decimal
from decimal import ROUND_HALF_UP

BASE_RATE = Decimal("30.00")
FAT_STEP_VALUE = Decimal("0.40")
SNF_STEP_VALUE = Decimal("0.30")
STANDARD_FAT = Decimal("3.5")
STANDARD_SNF = Decimal("8.5")
QUALITY_STEP = Decimal("0.1")
CENT = Decimal("0.01")


def rate_per_litre(fat, snf):
    """Return the rounded rate using nearest whole quality increments."""
    fat_steps = ((fat - STANDARD_FAT) / QUALITY_STEP).quantize(
        Decimal("1"),
        rounding=ROUND_HALF_UP,
    )
    snf_steps = ((snf - STANDARD_SNF) / QUALITY_STEP).quantize(
        Decimal("1"),
        rounding=ROUND_HALF_UP,
    )
    return (
        BASE_RATE + fat_steps * FAT_STEP_VALUE + snf_steps * SNF_STEP_VALUE
    ).quantize(CENT)


def payout(litres, fat, snf):
    """Return the payment for one entry rounded to paisa."""
    return (litres * rate_per_litre(fat, snf)).quantize(
        CENT,
        rounding=ROUND_HALF_UP,
    )

entries = [
    (Decimal("10"), Decimal("3.5"), Decimal("8.5")),
    (Decimal("8.5"), Decimal("4.2"), Decimal("8.7")),
    (Decimal("12"), Decimal("3.1"), Decimal("8.3")),
]

total = Decimal("0.00")
print(f"{'Entry':>5} {'Rate':>8} {'Payment':>10} {'Running total':>15}")
for index, entry in enumerate(entries, start=1):
    litres, fat, snf = entry
    rate = rate_per_litre(fat, snf)
    amount = payout(litres, fat, snf)
    total += amount
    print(f"{index:>5} {rate:>8.2f} {amount:>10.2f} {total:>15.2f}")

print(f"Three-entry total: Rs {total:.2f}")
