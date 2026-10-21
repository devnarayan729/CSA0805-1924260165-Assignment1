from collections.abc import Iterable
from decimal import Decimal, ROUND_HALF_UP

BASE_RATE = Decimal("30.00")
STANDARD_FAT = Decimal("3.5")
STANDARD_SNF = Decimal("8.5")
QUALITY_STEP = Decimal("0.1")
FAT_STEP_VALUE = Decimal("0.40")
SNF_STEP_VALUE = Decimal("0.30")
CENT = Decimal("0.01")

NumericInput = Decimal | int | float | str
MilkEntry = tuple[NumericInput, NumericInput, NumericInput]


def _to_decimal(value: NumericInput) -> Decimal:
    """Convert a numeric input to Decimal without importing float artifacts."""
    if isinstance(value, Decimal):
        return value
    return Decimal(str(value))


def _quality_steps(value: NumericInput, standard: Decimal) -> Decimal:
    """Return the nearest whole number of 0.1% steps from a standard value."""
    difference = (_to_decimal(value) - standard) / QUALITY_STEP
    return difference.quantize(Decimal("1"), rounding=ROUND_HALF_UP)


def rate_per_litre(fat: NumericInput, snf: NumericInput) -> Decimal:
    """Return the rate per litre, rounded to two decimal places."""
    fat_adjustment = _quality_steps(fat, STANDARD_FAT) * FAT_STEP_VALUE
    snf_adjustment = _quality_steps(snf, STANDARD_SNF) * SNF_STEP_VALUE
    return (BASE_RATE + fat_adjustment + snf_adjustment).quantize(CENT)


def payout(litres: NumericInput, fat: NumericInput, snf: NumericInput) -> Decimal:
    """Return the payment for one milk entry, rounded to the nearest paisa."""
    quantity = _to_decimal(litres)
    return (quantity * rate_per_litre(fat, snf)).quantize(
        CENT,
        rounding=ROUND_HALF_UP,
    )


def ten_day_total(entries: Iterable[MilkEntry]) -> Decimal:
    """Return the rounded total payment for a farmer's ten-day entries."""
    total = sum(
        (payout(litres, fat, snf) for litres, fat, snf in entries),
        Decimal("0.00"),
    )
    return total.quantize(CENT, rounding=ROUND_HALF_UP)


if __name__ == "__main__":
    entries = [
        (Decimal("10"), Decimal("3.5"), Decimal("8.5")),
        (Decimal("8.5"), Decimal("4.2"), Decimal("8.7")),
        (Decimal("12"), Decimal("3.1"), Decimal("8.3")),
    ]

    print(f"{'Litres':>8} {'Fat':>6} {'SNF':>6} {'Rate':>8} {'Payment':>10}")
    for litres, fat, snf in entries:
        rate = rate_per_litre(fat, snf)
        amount = payout(litres, fat, snf)
        print(f"{litres:>8} {fat:>6} {snf:>6} {rate:>8.2f} {amount:>10.2f}")

    print(f"Ten-day total: Rs {ten_day_total(entries):.2f}")