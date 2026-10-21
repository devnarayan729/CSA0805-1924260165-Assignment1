import math
from decimal import Decimal, ROUND_HALF_UP

print((4.2 - 3.5) / 0.1)
print(0.1 + 0.2 == 0.3)
print(-7 // 2)
print("int:", int(-3.9))
print("floor:", math.floor(-3.9))
print("round:", round(2.5))

def steps(value, standard):
    difference = Decimal(str(value)) - Decimal(str(standard))
    return int(
        (difference / Decimal("0.1")).quantize(
            Decimal("1"),
            rounding=ROUND_HALF_UP
        )
    )

for fat in (4.2, 3.1):
    fat_steps = steps(fat, 3.5)
    adjustment = Decimal(fat_steps) * Decimal("0.40")
    print(f"Fat: {fat}, Steps: {fat_steps}, "
          f"Adjustment: ₹{adjustment:.2f}")