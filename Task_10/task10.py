from decimal import Decimal
from decimal import ROUND_HALF_UP
from random import Random
from time import perf_counter

BASE_RATE = Decimal("30.00")
FAT_STEP_VALUE = Decimal("0.40")
SNF_STEP_VALUE = Decimal("0.30")
STANDARD_FAT = Decimal("3.5")
STANDARD_SNF = Decimal("8.5")
QUALITY_STEP = Decimal("0.1")
CENT = Decimal("0.01")

QUALITY_PAIRS = (
    (Decimal("3.5"), Decimal("8.5")),
    (Decimal("4.2"), Decimal("8.7")),
    (Decimal("3.1"), Decimal("8.3")),
)
LITRES = (
    Decimal("10"),
    Decimal("8.5"),
    Decimal("12"),
    Decimal("0.1"),
    Decimal("7.3"),
)
SIZES = (300, 6000, 150000)


def rate_per_litre(fat, snf):
    """Calculate the rate using Decimal quality increments."""
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
    ).quantize(CENT, rounding=ROUND_HALF_UP)


def payout(litres, fat, snf):
    """Return an entry payment rounded to the nearest paisa."""
    return (litres * rate_per_litre(fat, snf)).quantize(
        CENT,
        rounding=ROUND_HALF_UP,
    )


def rate_per_litre_float(fat, snf):
    """Calculate a comparison rate using binary floating-point arithmetic."""
    fat_steps = round((float(fat) - 3.5) / 0.1)
    snf_steps = round((float(snf) - 8.5) / 0.1)
    return round(30.0 + fat_steps * 0.4 + snf_steps * 0.3, 2)


def make_entries(count):
    """Create deterministic test entries with three repeated quality pairs."""
    generator = Random(42)
    return [
        (generator.choice(LITRES), *generator.choice(QUALITY_PAIRS))
        for _ in range(count)
    ]


def decimal_total(entries):
    """Return the sum of individually rounded Decimal payouts."""
    return sum((payout(*entry) for entry in entries), Decimal("0.00"))


def float_total(entries):
    """Return the sum of individually rounded float payouts."""
    total = 0.0
    for litres, fat, snf in entries:
        rate = rate_per_litre_float(fat, snf)
        total += round(float(litres) * rate, 2)
    return total


def cached_total(entries):
    """Calculate payouts with a rate dictionary keyed by fat and SNF."""
    rates = {}
    total = Decimal("0.00")
    for litres, fat, snf in entries:
        key = (fat, snf)
        if key not in rates:
            rates[key] = rate_per_litre(fat, snf)
        total += (litres * rates[key]).quantize(Decimal("0.01"))
    return total, len(rates)


def measure(function, entries):
    """Return the result and elapsed wall-clock seconds."""
    start = perf_counter()
    result = function(entries)
    return result, perf_counter() - start


def main():
    """Compare totals and timings at the three requested data sizes."""
    print(f"{'Entries':>9} {'Decimal total':>18} {'Float total':>18} {'Difference':>14}")
    for count in SIZES:
        entries = make_entries(count)
        exact, decimal_seconds = measure(decimal_total, entries)
        floating, float_seconds = measure(float_total, entries)
        raw_difference = Decimal.from_float(floating) - exact
        print(
            f"{count:>9} {exact:>18.2f} {floating:>18.2f} "
            f"{raw_difference:>14.6E}"
        )
        print(
            f"Decimal time={decimal_seconds:.6f}s, "
            f"float time={float_seconds:.6f}s"
        )

    repeated_entries = make_entries(150000)
    uncached, uncached_seconds = measure(decimal_total, repeated_entries)
    cached_result, cached_seconds = measure(cached_total, repeated_entries)
    cached, unique_rates = cached_result
    assert uncached == cached
    print(
        f"Rate cache: {unique_rates} unique pairs, "
        f"same total Rs {cached:.2f}; "
        f"uncached={uncached_seconds:.6f}s, cached={cached_seconds:.6f}s"
    )

    fractional_entries = [
        (Decimal("0.005"), Decimal("3.6"), Decimal("8.7"))
    ] * 5
    exact_unrounded_sum = sum(
        (litres * rate_per_litre(fat, snf) for litres, fat, snf in fractional_entries),
        Decimal("0.00"),
    )
    rounded_each = decimal_total(fractional_entries)
    rounded_once = exact_unrounded_sum.quantize(Decimal("0.01"))
    print(
        f"Rounding example: each payment={rounded_each:.2f}, "
        f"round once={rounded_once:.2f}"
    )


if __name__ == "__main__":
    main()
