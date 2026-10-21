from decimal import Decimal, InvalidOperation

def read_decimal(prompt):
    while True:
        try:
            return Decimal(input(prompt).strip())
        except InvalidOperation:
            print("Invalid number. Example: 8.5")

farmer_id = input("Farmer ID: ")
shift = input("Shift: ").strip().lower()

litres = read_decimal("Litres: ")
fat = read_decimal("Fat percentage: ")
snf = read_decimal("SNF percentage: ")

if litres <= 0:
    print("Invalid quantity.")
elif not Decimal("2.0") <= fat <= Decimal("7.0"):
    print("Invalid fat percentage.")
elif not Decimal("0.0") <= snf <= Decimal("20.0"):
    print("Invalid SNF percentage.")
else:
    print(f"{'Farmer':<12}{'Shift':<12}")
    print(f"{farmer_id:<12}{shift:<12}")
    print("Entry accepted.")