#Basic input,indentation,if,variable,operation and error lessons

#print("Hello world")
#number_1 = 8
#number_2 = 10
#add = number_1 + number_2
print("Pay Check Calculator")

hours = int(input("Hours Worked: "))
rate = float(input("Hourly Pay Rate: "))
grosspay = hours * rate
print(f"Gross Pay: {grosspay}")
print("Gross Pay:", grosspay)
# OR like print("The grosspay is =, grosspay")
tax_rate = float(input("Tax Rate:"))
print(f"Tax Rate:{tax_rate}%")
    
tax = grosspay * (tax_rate/100)
print(f"Tax Amount: {tax}")
cash_in_hand = grosspay - tax
print(f"Take Home Pay: {cash_in_hand}")
print("--------------")
#
# use +\ to extend the line to next one
# ''' something ............ ''' also means comments
