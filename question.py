 #First i asked the user to input his marks in 4 different subjects and defined it iwth 4 different variables
#Then i used / to continue in another as described in question
#lastly i used end function as described in the question

math = float(input("please input your score in maths?\n"))
science = float(input("please input your score in science?\n"))
english = float(input("please input your score in english?\n"))
python = float(input("please input your score in python?\n"))

sum = (math + science + english +\
       python)
print(f"Your toatl score is {sum}",end="***")



a = 6
b = 2
c = 3
f = (b *c) - a
print(f)

print("Tip Calculator")
cost = float(input("Cost of Meal: "))
Tip_percent = float(input("Tip Percent:"))

amount = round(cost * (Tip_percent/100) , 2)
print(f"Tip Amount: {amount}")
total = round(cost + amount , 2)
print(f"Toatl Amount: {total}")

mile = float(input("Please enter the no. of miles drivern: "))
gallons = float(input("Please enter the no. of gallons consumed by the vehicle: "))
mpg = round(mile/gallons,2)
print("The mpg value of your vehicle is" , mpg)