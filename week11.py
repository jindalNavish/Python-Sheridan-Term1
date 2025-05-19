""" jod = 0
def hunk(jod):
    god = int(input("Enter the sales amount: "))
    jod += god
    return  jod

keep_going = 'y'
while keep_going == 'y' or keep_going =='Y':
    sales_amount = hunk(jod) 
    while sales_amount<0:
        print("The sales amount must be greter than 0. Please, try again.")
        sales_amount = hunk(jod)
    if sales_amount> 1000:
        bonus = 200
    elif sales_amount > 600:
        bonus = 160
    elif sales_amount > 300:
        bonus = 100
    else:
        bonus = 0
    print(f"The bonus amount is ${bonus}")
    keep_going = input("Do you want to process another employee?(y/n)")
print("Thanks")




def myname():
    my_name = "Navish"
    print(my_name)
    
myname()

def mpg_cal(miles,gallons):
    mpg = miles/gallons
    mpg = round(mpg,1)
    return mpg

miles,gallons = input("Please, enter the values of miles driven and the gallons: ").split()
miles,gallons = float(miles),float(gallons)
mpg = mpg_cal(miles,gallons)
print("The value of mpg is:",mpg) 
 """
""" def grosspay(hours, rate):
    grosspay = hours * rate
    return grosspay

def main():
    hours_worked,pay_rate = input("enter the hours worked and the pay rate: ").split(",")
    hours_worked,pay_rate = float(hours_worked),float(pay_rate)
    print("The grosspay is ",grosspay(hours_worked, pay_rate))
    
if __name__ == "__main__":
    main() """

def showbonus(emp_name,income,yox):
    if income >= 40000 and yox>= 5:
        print(emp_name + " qualifies for a bonus of $4000")
    elif income >=40000 and yox<5:
        print(emp_name," You qualify for a bonus of $2000")
    else:
        print("You don't qualify")
        
def main():
    emp_name,income,yox = input("Enter your name, your income and your years of experience: ").split(",")
    income,yox = float(income),float(yox)
    showbonus(emp_name,income,yox)
    
if __name__ == "__main__":
    main()