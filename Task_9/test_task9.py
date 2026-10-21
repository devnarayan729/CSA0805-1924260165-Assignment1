from decimal import Decimal

from Task_9.calculator import (
    calculate_payout,
    parse_decimal,
    rate_per_litre,
    validate_entry,
)

VALID = ("F001", Decimal("10"), Decimal("3.5"), Decimal("8.5"), "morning")


def run_tests():
    """Run the calculator's acceptance and validation checks."""
    cases = [
        ("standard", Decimal("30.00"), rate_per_litre(Decimal("3.5"), Decimal("8.5"))),
        ("fat and SNF above", Decimal("33.40"), rate_per_litre(Decimal("4.2"), Decimal("8.7"))),
        ("fat and SNF below", Decimal("27.80"), rate_per_litre(Decimal("3.1"), Decimal("8.3"))),
        ("minimum fat", Decimal("24.00"), rate_per_litre(Decimal("2.0"), Decimal("8.5"))),
        ("maximum fat", Decimal("44.00"), rate_per_litre(Decimal("7.0"), Decimal("8.5"))),
        ("standard payout", Decimal("300.00"), calculate_payout(Decimal("10"), Decimal("3.5"), Decimal("8.5"))),
    ]

    five_entries = [
        (Decimal("10"), Decimal("3.5"), Decimal("8.5")),
        (Decimal("8.5"), Decimal("4.2"), Decimal("8.7")),
        (Decimal("12"), Decimal("3.1"), Decimal("8.3")),
        (Decimal("5"), Decimal("2.0"), Decimal("8.5")),
        (Decimal("7"), Decimal("7.0"), Decimal("8.5")),
    ]
    five_total = sum(
        (calculate_payout(*entry) for entry in five_entries),
        Decimal("0.00"),
    )
    cases.append(("five-entry hand total", Decimal("1345.50"), five_total))

    for name, expected, actual in cases:
        assert expected == actual, f"{name}: expected {expected}, got {actual}"
        print(f"PASS {name}: expected={expected:.2f}, actual={actual:.2f}")

    assert parse_decimal(" 8.5 ") == Decimal("8.5")
    print("PASS whitespace numeric parsing: 8.5")

    invalid_values = ("eight", "8,5", "NaN", "Infinity")
    for text in invalid_values:
        try:
            parse_decimal(text)
        except ValueError:
            print(f"PASS rejected invalid decimal: {text}")
        else:
            raise AssertionError(f"Expected {text!r} to be rejected")

    invalid_entries = [
        ("negative quantity", ("F001", Decimal("-1"), Decimal("3.5"), Decimal("8.5"), "morning")),
        ("low fat", ("F001", Decimal("1"), Decimal("1.9"), Decimal("8.5"), "morning")),
        ("high fat", ("F001", Decimal("1"), Decimal("7.1"), Decimal("8.5"), "morning")),
    ]
    for name, entry in invalid_entries:
        try:
            validate_entry(*entry)
        except ValueError:
            print(f"PASS rejected {name}")
        else:
            raise AssertionError(f"Expected {name} to be rejected")


if __name__ == "__main__":
    run_tests()
