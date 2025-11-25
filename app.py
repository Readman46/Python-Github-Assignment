print("Welcome to my Python program!")

amount = input("How much money did you make today? $")

amount = float(amount)
weekly_total = amount * 7

print(f"If you make this amount every day, you'll make ${weekly_total:.2f} this week!")