from dataclasses import dataclass
from decimal import Decimal, ROUND_HALF_UP

CENT = Decimal("0.01")
STANDARD_FAT = Decimal("3.50")
STANDARD_SNF = Decimal("8.50")
QUALITY_STEP = Decimal("0.10")
FAT_STEP_REGULAR = Decimal("0.40")
SNF_STEP_VALUE = Decimal("0.30")
MIN_FAT = Decimal("2.00")
MAX_FAT = Decimal("7.00")
MIN_SNF = Decimal("0.00")
MAX_SNF = Decimal("20.00")
BONUS_THRESHOLD_LITRES = Decimal("500")
BONUS_PER_LITRE = Decimal("0.50")


@dataclass(frozen=True)
class RateCard:
    """Rates for a single operating season."""

    base_rate: Decimal
    fat_step_value: Decimal
    snf_step_value: Decimal


RATE_CARDS = {
    "regular": RateCard(
        base_rate=Decimal("30.00"),
        fat_step_value=FAT_STEP_REGULAR,
        snf_step_value=SNF_STEP_VALUE,
    ),
    "april_june": RateCard(
        base_rate=Decimal("32.00"),
        fat_step_value=Decimal("0.45"),
        snf_step_value=SNF_STEP_VALUE,
    ),
}


def _decimal(value):
    """Convert a decimal-compatible value without binary float artifacts."""
    if isinstance(value, Decimal):
        return value
    return Decimal(str(value))


def validate_measurements(litres, fat, snf):
    """Raise ValueError when the quantity or analyser readings are invalid."""
    if litres <= 0:
        raise ValueError("Litres must be greater than zero.")
    if not MIN_FAT <= fat <= MAX_FAT:
        raise ValueError("Fat must be between 2.00% and 7.00%.")
    if not MIN_SNF <= snf <= MAX_SNF:
        raise ValueError("SNF must be between 0.00% and 20.00%.")


def rate_per_litre(fat, snf, season="regular"):
    """Calculate a two-decimal rate using the selected seasonal rate card."""
    try:
        card = RATE_CARDS[season]
    except KeyError as error:
        raise ValueError(f"Unknown season: {season!r}") from error

    fat_steps = ((fat - STANDARD_FAT) / QUALITY_STEP).quantize(
        Decimal("1"),
        rounding=ROUND_HALF_UP,
    )
    snf_steps = ((snf - STANDARD_SNF) / QUALITY_STEP).quantize(
        Decimal("1"),
        rounding=ROUND_HALF_UP,
    )
    amount = (
        card.base_rate
        + fat_steps * card.fat_step_value
        + snf_steps * card.snf_step_value
    )
    return amount.quantize(CENT, rounding=ROUND_HALF_UP)


def bonus_for_ten_day_volume(total_litres):
    """Return the ten-day volume bonus for more than 500 litres."""
    if total_litres > BONUS_THRESHOLD_LITRES:
        return (total_litres * BONUS_PER_LITRE).quantize(
            CENT,
            rounding=ROUND_HALF_UP,
        )
    return Decimal("0.00")


def calculate_ten_day_payment(entries, season="regular"):
    """Return detail rows and the total including any ten-day volume bonus."""
    total_litres = sum((entry[0] for entry in entries), Decimal("0"))
    rows = []
    total_milk_pay = Decimal("0.00")
    for litres, fat, snf in entries:
        validate_measurements(litres, fat, snf)
        rate = rate_per_litre(fat, snf, season)
        payment = (litres * rate).quantize(CENT, rounding=ROUND_HALF_UP)
        rows.append((litres, fat, snf, rate, payment))
        total_milk_pay += payment

    bonus = bonus_for_ten_day_volume(total_litres)
    return rows, total_litres, bonus, total_milk_pay + bonus


def main():
    """Print sample results for both seasons and the bonus threshold."""
    entries = [(Decimal("501"), Decimal("4.23"), Decimal("8.57"))]
    expected_rates = {
        "regular": Decimal("33.10"),
        "april_june": Decimal("35.45"),
    }
    expected_totals = {
        "regular": Decimal("16833.60"),
        "april_june": Decimal("18010.95"),
    }
    for season in RATE_CARDS:
        rows, litres, bonus, total = calculate_ten_day_payment(entries, season)
        rate = rows[0][3]
        assert rate == expected_rates[season]
        assert total == expected_totals[season]
        assert bonus == Decimal("250.50")
        print(
            f"{season}: litres={litres}, rate={rate:.2f}, "
            f"milk pay={rows[0][4]:.2f}, bonus={bonus:.2f}, total={total:.2f}"
        )
    no_bonus = bonus_for_ten_day_volume(Decimal("500"))
    assert no_bonus == Decimal("0.00")
    print(f"Bonus at exactly 500 L: {no_bonus:.2f}")


if __name__ == "__main__":
    main()
