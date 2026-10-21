import sys
from decimal import Decimal

payments = ["33.40"] * 1000 + ["0.10"] * 3


def total_float(items):
    total = 0.0
    for amount in items:
        total += float(amount)
    return total


def total_decimal(items):
    return sum((Decimal(amount) for amount in items), Decimal("0.00"))


def total_paise(items):
    return sum(int(Decimal(amount) * 100) for amount in items)


def total_rounded_float(items):
    total = 0.0
    for amount in items:
        total = round(total + float(amount), 2)
    return total


if __name__ == "__main__":
    values = (10, 10.0, "10", True, [10, 8.5])
    for value in values:
        print(f"type({value!r}) = {type(value).__name__}")

    print("7 / 2 =", 7 / 2)
    print("7 // 2 =", 7 // 2)
    print("7 % 2 =", 7 % 2)
    print("-7 // 2 =", -7 // 2)
    print("0.1 + 0.2 == 0.3 =", 0.1 + 0.2 == 0.3)
    print("Decimal equality =", Decimal("0.1") + Decimal("0.2") == Decimal("0.3"))
    print("float  :", total_float(payments))
    print("Decimal:", total_decimal(payments))
    print("Integer paise:", total_paise(payments))
    print("Rounded float:", total_rounded_float(payments))
    print("Decimal(float('0.1')):", Decimal(float("0.1")))
    print("sys.getsizeof(int paise):", sys.getsizeof(total_paise(payments)))
    print("sys.getsizeof(float rupees):", sys.getsizeof(total_float(payments)))
    print("sys.getsizeof(Decimal rupees):", sys.getsizeof(total_decimal(payments)))
