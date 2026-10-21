"""Demonstrate importing and using the milk rate module."""

from decimal import Decimal

import milkrate as mr

litres = Decimal("8.5")
fat = Decimal("4.2")
snf = Decimal("8.7")

print(f"Rate per litre: Rs {mr.rate_per_litre(fat, snf):.2f}")
print(f"Payout: Rs {mr.payout(litres, fat, snf):.2f}")
