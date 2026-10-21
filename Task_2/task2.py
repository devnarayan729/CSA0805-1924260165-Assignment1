from decimal import Decimal

print(type(10))
print(type(10.0))
print(type("10"))
print(type(True))
print(type([10, 8.5]))

print(7 / 2)
print(7 // 2)
print(7 % 2)
print(-7 // 2)

print(0.1 + 0.2 == 0.3)
print(Decimal("0.1") + Decimal("0.2"))

payments = ["33.40"] * 1000 + ["0.10"] * 3

float_total = sum(float(x) for x in payments)
decimal_total = sum(
    (Decimal(x) for x in payments),
    Decimal("0.00")
)

print("Float total:", float_total)
print("Decimal total:", decimal_total)