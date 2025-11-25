print("Welcome to my Python program!")

#This code is the input function where the user inputs how much money they made
amount = input("How much money did you make today? $")

#This code is used toexit the code if the user enters something that isnt a number
try:
    amount = float(amount)
except ValueError:
    print("Please enter a valid number.")
    exit()

#This multiplies the users number by seven to simulate a week
amount = float(amount)
weekly_total = amount * 7

#This final part prints how much money theyd make in a week if their daily incomme is consistent
print(f"If you make this amount every day, you'll make ${weekly_total:.2f} this week!")