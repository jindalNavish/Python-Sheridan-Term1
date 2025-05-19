score = float(input("Enter your marks: "))

if score >= 90:
    Letter = "A"
elif score >= 80:
    Letter = "B"
elif score >= 70:
    Letter = "C"
elif score >= 60:
    Letter = "D"
else:
    Letter = "F"
print(f"Your mark letter is {Letter}.")

salary = float(input("Enter your salary:"))
years = float(input("Enter years on job:"))
if salary >= 30000:
    if years >= 2:
        print("You qualify for the loan")
    else:
        print("You must have atleast 2 years on job to qualify for the loan")
else:
    print("You must earn at least $30000 per year to qualify for the loan")
    
age = int(input("Enter your age: "))
ticket = float(input("Enter the ticket price: "))
if age >= 65 or age <= 12:
    discount_price = 0.25
    discounted_amount = ticket * discount_price
    fare = ticket - discounted_amount
else:
    fare = ticket
print(f"Please,pay ${fare}.")   

print("Tip Calculator")

cost = float(input("Cost of Meal: "))

tip_amount = round((15/100) * cost,2)
total = cost + tip_amount
print("15%")
print(f"Tip amount:  {tip_amount}" )
print(f"Total amount:  {total}")

tip_amount_1 = round((20/100) * cost,2)
total_1 = cost + tip_amount_1
print("20%")
print(f"Tip amount:  {tip_amount_1}" )
print(f"Total amount:  {total_1}")

tip_amount_2 = round((25/100) * cost,2)
total_2 = cost + tip_amount_2
print("25%")
print(f"Tip amount:  {tip_amount_2}" )
print(f"Total amount:  {total_2}")

import math as m
print(m.floor(3.95))
print(int(3.95))