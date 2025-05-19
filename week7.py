""" while True:
    s= int(input("What is your number?(postive numbers only)"))
    if s <= 0:
        continue
    if s > 0:
        break 
    
 # tupils   
pins = (2340,9034,7812,1209,5128,6205)
print(pins[3])
print(pins[-1])
print(pins[1:4])
x = pins[2]
info = "s2patel" + str(pins[4])
print("info" , sep=":")
print()

movie = ("Monty Python and Holy Grail", 1975, 5.99)
title, year, ticket = movie
print("With ${2} you could watch {0} in {1}.".format(title,year,ticket) )
print()

#pins[0] = "1239", tuples cant be changed unlike lists

# string as keys and values
countires = {1 : "Canada" , "US":9.99, "MX":"Mexico"}
print("countries:",countires)

book_catalog = {}
book_catalog["Boss up"] = 2019
book_catalog["Kasey and Ivy"] = 2018


book_catalog["Boss up"] = 2022
#changing value of key
book_catalog["Your Name"] = 2018
print(f"Book catalog: {book_catalog}")

book = "Your Name"

if book in book_catalog:
    code = book_catalog[book]
    print(code)
else:
    (f"The book is not in the databse: {book}") 

code1 = book_catalog.get("hn")
code2 = book_catalog.get("Boss up")
code3 = book_catalog.get("OK","Your key is not there in my dictionary")
print(code1)
print(code2)
print(code3)

Courses = {}
Courses["10058"]="Python"
Courses["10068"]="Maths"
Courses["10078"]="Technical"
Courses["10088"]="Data"

course_code = input("Enter the course code you want to check for?")

if course_code in Courses:
    Courses.pop(course_code,"There is no course for this code")
    print("The course is deleted")"""


eng_hin = {"ok":"acha","yes":"haan","no":"nahi"}
hin_pun = {"acha":"theeka","haan":"aaho","nahi":"nah"}

user = input("Enter a word you want to translate in english: ")

if user in eng_hin:
    output1 =eng_hin.get(user)
    output2 =hin_pun.get(output1)
    print(f"The hindi translation: {output1}, The punjabi translation: {output2}")
else:
    print("Not in dictionary")
    trans1,trans2 = input("What do you think the translation of this word is in hindi and punjabi? ").split(",")
    eng_hin[user] = trans1
    hin_pun[trans1] = trans2
    print(f"The hindi translation is {trans1}, The punjabi trasnlation is {trans2}")
