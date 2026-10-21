from decimal import Decimal, InvalidOperation

MIN_FAT = Decimal("2.0")
MAX_FAT = Decimal("7.0")
MIN_SNF = Decimal("0.0")
MAX_SNF = Decimal("20.0")


def read_decimal(prompt):
    while True:
        text = input(prompt).strip()
        try:
            value = Decimal(text)
            if not value.is_finite():
                raise InvalidOperation
            return value
        except InvalidOperation:
            print("Enter a valid decimal number, for example 8.5.")


def read_entry():
    farmer_id = input("Farmer ID: ").strip()
    shift = input("Shift (morning/evening): ").strip().lower()
    litres = read_decimal("Litres: ")
    fat = read_decimal("Fat percentage: ")
    snf = read_decimal("SNF percentage: ")

    if not farmer_id:
        raise ValueError("Farmer ID cannot be empty.")
    if shift not in {"morning", "evening"}:
        raise ValueError("Shift must be morning or evening.")
    if litres <= 0:
        raise ValueError("Litres must be greater than zero.")
    if not MIN_FAT <= fat <= MAX_FAT:
        raise ValueError("Fat must be between 2.0% and 7.0%.")
    if not MIN_SNF <= snf <= MAX_SNF:
        raise ValueError("SNF must be between 0.0% and 20.0%.")
    return farmer_id, shift, litres, fat, snf


if __name__ == "__main__":
    try:
        farmer_id, shift, litres, fat, snf = read_entry()
        print(f"{'Farmer':<12}{'Shift':<12}{'Litres':>10}{'Fat':>8}{'SNF':>8}")
        print(f"{farmer_id:<12}{shift:<12}{litres:>10.2f}{fat:>8.2f}{snf:>8.2f}")
    except ValueError as error:
        print(f"Invalid entry: {error}")
