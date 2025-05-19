hours_day1 = int(input("Enter the number of hours in day 1:"))
hours_day2 = int(input("Enter the number of hours in day 2:"))
total_hours = hours_day1 + hours_day2
print(f"The total hours worked {total_hours}")

quantity = int(input("How many units are on the shelf?:"))

number1 , number2 = input("Enter the two number you want to multiply?").split(":")
# use split()for space and split("symbol") for asking the input with a symbol between
n01 , no2 = (float(number1),float(number2))
print(n01 * no2)


message = "You are really"
print(message[2])
print(message[-1])
print(message[8:])
print(message[1:9])
print(len(message)) 

date = "11/9.1972"
date = date.split("/")
#used to convert a string into a list
mecha ="I love vinland sage"
mecha = mecha.split()
day = int(date[0])
first = (mecha[0]) 
print(day , first)
ip = "192 16 098"
print(ip.strip("098"))
#strip can only be used from start or end 
print(ip.startswith("192"))
# You cant use a lot of attribuites with a list 

mega =("lmao nerd")
print(mega.title())
print(mega.islower())
print(mega.isupper())

#You can't use attributes with integers