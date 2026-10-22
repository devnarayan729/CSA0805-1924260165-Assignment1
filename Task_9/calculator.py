from decimal import Decimal, InvalidOperation

from Task_7.milkrate import payout as calculate_payout
from Task_7.milkrate import rate_per_litre

MIN_FAT = Decimal("2.0")
MAX_FAT = Decimal("7.0")
MIN_SNF = Decimal("0.0")
MAX_SNF = Decimal("20.0")


def parse_decimal(text):
    """Parse a finite decimal string or raise ValueError."""
    try:
        value = Decimal(text.strip())
    except (InvalidOperation, AttributeError) as error:
        raise ValueError(f"Invalid decimal value: {text!r}") from error
    if not value.is_finite():
        raise ValueError("Measurements must be finite numbers")
    return value


def validate_entry(farmer_id, litres, fat, snf, shift):
    """Validate the fields for one farmer milk entry."""
    if not farmer_id.strip():
        raise ValueError("Farmer ID cannot be empty.")
    if shift.strip().lower() not in {"morning", "evening"}:
        raise ValueError("Shift must be morning or evening.")
    if litres <= 0:
        raise ValueError("Litres must be greater than zero.")
    if not MIN_FAT <= fat <= MAX_FAT:
        raise ValueError("Fat must be between 2.0% and 7.0%.")
    if not MIN_SNF <= snf <= MAX_SNF:
        raise ValueError("SNF must be between 0.0% and 20.0%.")


def read_decimal(prompt):
    """Read a finite decimal value, retrying after invalid text."""
    while True:
        text = input(prompt)
        try:
            return parse_decimal(text)
        except ValueError as error:
            print(error)


def main():
    """Read entries and print their payments and total."""
    count = int(input("Number of entries: "))
    if count <= 0:
        raise ValueError("Number of entries must be positive.")

    total = Decimal("0.00")
    print(f"{'Farmer':<12}{'Shift':<10}{'Litres':>9}{'Rate':>9}{'Payment':>11}")
    for _ in range(count):
        farmer_id = input("Farmer ID: ").strip()
        shift = input("Shift (morning/evening): ").strip().lower()
        litres = read_decimal("Litres: ")
        fat = read_decimal("Fat percentage: ")
        snf = read_decimal("SNF percentage: ")
        validate_entry(farmer_id, litres, fat, snf, shift)
        rate = rate_per_litre(fat, snf)
        amount = calculate_payout(litres, fat, snf)
        total += amount
        print(f"{farmer_id:<12}{shift:<10}{litres:>9.2f}{rate:>9.2f}{amount:>11.2f}")

    print(f"Ten-day total: Rs {total:.2f}")


if __name__ == "__main__":
    main()
