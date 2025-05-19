#type class

n1 = 20
print(type(n1))
print(type("20"))

c=7.5
c = str(c)
print(c)

#str to int not possible

grade1= 91
grade2= 83
grade3= 96

average = grade1 + grade2 + grade3/3
print(average)

name = input("Please enter your name?\n").lower()


import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

user_letters = int(input("How many letters would like in your password\n"))
user_numbers = int(input("How many numbers would like in your password\n"))
user_symbols = int(input("How many symbols would like in your password\n"))
user_pass = []

for char in range(1,user_letters + 1):
    user_pass += random.choice(letters)
for char in range(1,user_numbers + 1):
    user_pass += random.choice(numbers)
for char in range(1,user_symbols + 1):
    user_pass += random.choice(symbols)
    
password = ""

random.shuffle(user_pass)
    
for char in user_pass:
    password += char
print(f"Welcome {name}!")
print("Your registration is complete")
print(f"Your temporary password is: {password}")

