entry = "12345"
entry_integer = entry.isdigit()

entry2 = "jod"
entry2_integer = entry2.isdigit()

movie = "The story of lionel"
movie_substring = movie.startswith("The")
movie_substring2 = movie.endswith("lionel")
movie_title = movie.title()

ip_address = "  192.180.22.223  "
ip_strip = ip_address.strip()

print(entry_integer)
print(entry2_integer)
print(movie_substring)
print(movie_substring2)
print(ip_strip)
print(movie_title)

print("king".ljust(10),"Navish".rjust(14))
#There is 24 spaces
print("king".ljust(0),"Navish".rjust(14))
# There is 14 spaces
print("king" , "Navish")
#adjust is used to formatt string better

address = ["Navish Jindal" , "192 inspire boulevard" , "Brampton" , "Ontario" , "L6R 0B3"]
address_join = "|".join(address)
print(address_join)
print(address_join.startswith("Navish"))
# Join is used to covert list to a string

Variable = "Sheridan"
Variable_join = " ".join(Variable)
print(Variable_join)

print("Title:\t\t Python Programming\nQuantity:\t5")
# \t to insert a tab  """

message = "JZCORP"
message_join = " ".join(message)
ammount = 456.45912

print(message_join)
print("Business Account")
print("a link to the file:\tC:\\users\\jzcorp\\ba.txt")
print("amount in dollar: {:.3f}".format(ammount))
# use backslash 2 time to put one backslash in the text


firstname = input("Please enter your first name: ")
lastname = input("please enter your last name: ")
print('%s%15s'%(firstname,lastname))
print('%14s%15s'%(firstname,lastname))
print('%-15s'%(firstname))
print('%5d%10d'%(15,45))
print('%15.3f'%(45.51235))
print('%15.3f'%(45.51235))

name = input("PLease enter your firstname : ")
marks1, marks2 ,marks3 , marks4  = input("Please enter your grades in subject1 ,subject2 ,subject3 ,subject4 respectively: ").split(":")
mark1, mark2 ,mark3 , mark4 = (float(marks1),float(marks2),float(marks3),float(marks4))
Average = (mark1 + mark2 + mark3 + mark4)/4
#if Average >=50:
    #print(f"{name},your pass status is: True" )
#else:
    #Print(f"{name},your pass status is: False")
print(f"{name}, your pass status is: {Average >= 50}")

print('one'
      'two')


