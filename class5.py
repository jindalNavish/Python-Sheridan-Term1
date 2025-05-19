grade = float(input("Enter your grade: "))
if grade >= 50:
    print("passed")
else:
    print("fail")
    
import math as m 
x = m.ceil(3.24)
print(x)
print("jod" + (
"ha"))

vince = "  Guyyy  "
print(vince.center(5))

print(vince.find("Gu"))

user_name= ["goat",2569,"goat2","goat3"]

student_1 = user_name[0] + "99123"
student_2 = user_name[1] + 99231
student_3 = user_name[2] + "99321"
student_4 = user_name[3] + "99542"

print("student1_information" ,student_1, sep='/')
print("student2_information" ,student_2, sep='/')
print("student3_information" ,student_3, sep='/')
print("student4_information" ,student_4, sep='/')

numbers = [52 , 54 ,56 , 58, 60, 62]
print(numbers[::-1])
print(numbers[0:4:2])
print(numbers[:2])
print(numbers[0:2])
print(numbers[3:])

list_one = [1 , 3, 4, 5, 9]
list_two = list_one
list_one[1] = 11
print(list_one)
print(list_two)
#when two lists are equal the change in one list result to change in other aswell

import copy
list_1 = [1 , 7, 8, 2, 9]
list_2 = copy.deepcopy(list_1)
list_2[1] = 11
print(list_1)
print(list_2)

#But with deepcopy the other list copies the first list fully and is a seperate list afterwords therefore changes made to one
#doesen't alter other.

inventory = ["god" , "bot", 1569, "ok"]
print("inventory:  ", inventory)

inventory.insert(3, 1785)
print("inventory after inserting:  ",inventory)

remove_ = inventory.remove("ok")
print("inventory after remove:  ", inventory)

inventory.append("Hmmmm")
print("inventory after append:  ", inventory)

pop_ = inventory.pop(1)
print("inventory after pop:  ", inventory)
print(pop_)
print(remove_)
#pop returns the deleted item but remove doesen't

foodlist = ["orange","banana","Pear","banana"]
foodlist.sort()
print(foodlist)
foodlist.sort(key=str.lower)
print(foodlist)

inventory.extend(foodlist)
print("inventory after extend:" , inventory)
print(len(inventory))
# retuns item in this list

numlist = [70 , 2 ,56 ,58, 84, 11]
minimum = min(numlist)
print('The minimum value: ', minimum)

maximum = max(numlist)
print('The maximum value: ', maximum)

total_1 = sum(numlist)
print('The sum value: ', total_1)
total_2 =sum(numlist , start=100)
print('The sum value after adding 100: ', total_2)

inventory.extend(numlist)

last_name = input("Enter your last name: ")
mylist = list(last_name)
print(mylist)
enum = enumerate(mylist)
print(enum)

first_name, last_name, student_id = input("Enter your first name, last name, student id:").split(":")
empty_list = []
empty_list.append(first_name) 
empty_list.append(last_name)
empty_list.append(student_id)
print(empty_list) 

sale_1 , sale_2 , sale_3, sale_4 = input("Enter 4 sales amount: ").split(",")
sales_1 , sales_2 , sales_3, sales_4 = (float(sale_1),float(sale_2),float(sale_3),float(sale_4))
sale_list = []
sale_list.append(sales_1)
sale_list.append(sales_2)
sale_list.append(sales_3)
sale_list.append(sales_4)
print("List:",sale_list)

high = max(sale_list)
print("maximum:",high)
low = min(sale_list)
print("minimum:",low)
total = sum(sale_list)
print("sum:",total)

sale_sort = sale_list.sort()
print("sort:",sale_list)
sale_sort2 = sale_list.reverse()
print("reverse:" ,sale_list)

count_item = sale_list.count(45)
print(count_item)

import random
num_list = [15, 75, 85, 90, 78, 65]
choice = random.choice(num_list)
shuffle = random.shuffle(num_list)
print(choice)
print(num_list)

item = 75
if item in num_list:
    num_list.remove(item)
print(num_list)

num_item = 15

if num_item in num_list:
    print(f"Yes,{num_item} is in the list" )
else:
    print(f"NO,{num_item} is not in the list" )
    
fruits = ["apple", "banana", "cherry", "date"]

# Check if a specific fruit is in the list using the in keyword
fruit_to_check = input("Enter the fruit you want to check: ")

# Using if statement with in keyword
if fruit_to_check in fruits:
    print(f"Yes, {fruit_to_check} is in the list of fruits.")
else:
    print(f"No, {fruit_to_check} is not in the list of fruits.")

fruit_to_check_2 = input("Enter the fruit: ")

if fruit_to_check_2 not in fruits:
    fruits.append(fruit_to_check_2)
print(fruits) 

print(list(range(4)))
list_1 = list(range(5,13))
print(list_1)
list_2 = list(range(5,13,2))
print(list_2)

numbers = [10, 20 ,30 ,40 ,50, 60, 70 ,80 ,90, 100]
indices = range(len(numbers))
print(indices)

if 0 in indices:
    print(f"Element at index 0 is: {numbers[0]}")

if 9 in indices:
    print(f"Element at index 0 is: {numbers[9]}")
    
index_check = 5

if index_check in indices:
    print(f"Element at index{index_check} = {numbers[5]}")
    
index_check = 10

if index_check in indices:
    print(f"Element at index{index_check} = {numbers[10]}")
else:
    print("Out of Range")
