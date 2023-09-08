from decimal import Decimal

while True:
    try:
        n = Decimal(input("What is your favorite number?"))
    except ValueError:
        print("That's not a number!")
    else:
        print(f"Oh {n} is a lovely number!")
