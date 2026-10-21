"""Rate card and payment calculations for the village milk co-operative."""

from decimal import Decimal, ROUND_HALF_UP

BASE_RATE = Decimal("30.00")
FAT_STEP_VALUE = Decimal("0.40")
SNF_STEP_VALUE = Decimal("0.30")
STANDARD_FAT = Decimal("3.5")
STANDARD_SNF = Decimal("8.5")
QUALITY_STEP = Decimal("0.1")
CENT = Decimal("0.01")

NumericInput = Decimal | int | float | str


def _decimal(value: NumericInput) -> Decimal:
    """Convert a supported numeric input to Decimal."""
    if isinstance(value, Decimal):
        return value
    return Decimal(str(value))


def _quality_steps(value: NumericInput, standard: Decimal) -> Decimal:
    """Return the nearest whole number of quality increments from standard."""
    increments = (_decimal(value) - standard) / QUALITY_STEP
    return increments.quantize(Decimal("1"), rounding=ROUND_HALF_UP)


def rate_per_litre(fat: NumericInput, snf: NumericInput) -> Decimal:
    """Return the rate per litre, rounded to two decimal places."""
    rate = (
        BASE_RATE
        + _quality_steps(fat, STANDARD_FAT) * FAT_STEP_VALUE
        + _quality_steps(snf, STANDARD_SNF) * SNF_STEP_VALUE
    )
    return rate.quantize(CENT, rounding=ROUND_HALF_UP)


def payout(
    litres: NumericInput,
    fat: NumericInput,
    snf: NumericInput,
) -> Decimal:
    """Return the payment for the supplied milk entry, rounded to paisa."""
    return (_decimal(litres) * rate_per_litre(fat, snf)).quantize(
        CENT,
        rounding=ROUND_HALF_UP,
    )


if __name__ == "__main__":
    sample_entries = [
        (Decimal("10"), Decimal("3.5"), Decimal("8.5")),
        (Decimal("8.5"), Decimal("4.2"), Decimal("8.7")),
        (Decimal("12"), Decimal("3.1"), Decimal("8.3")),
    ]

    for litres, fat, snf in sample_entries:
        rate = rate_per_litre(fat, snf)
        amount = payout(litres, fat, snf)
        print(
            f"{litres:5} L  fat {fat}  snf {snf}  "
            f"rate {rate:6.2f}  pay {amount:8.2f}"
        )
