""" subject1,subject2,subject3 = input("Input the 3 subjects:").split(",")
subject = list[subject1,subject2,subject3]
grade1,grade2,grade3 = input("Input the 3 grades:").split(",")
grades = list[grade1,grade2,grade3]
print(grades,subject)
end_list = subject.extend(grades)
print(subject)
subject_remove = "python"

if subject_remove in subject:
    subject_index = subject.index("python")
    subject.pop(subject_index)
    garde_index = subject_index + 2
    grade_index_ok = subject_index
    grades.pop(subject_index)
    subject.pop(garde_index)
print(subject)

subject_remove = "Technical"
if subject_remove not in subject:
    subject.insert(2,subject_remove)
    subject.append(85)
    grades.append(85)
print(subject)

average = sum(grades)/3
new_list = []
new_list.extend(subject)
new_list.append(average)
print(new_list)

if average >= 90:
    print("You achieved Grade A")

elif average >= 80:
    print("You achieved Grade B")

elif average >= 70:
    print("You achieved Grade C")

elif average >= 60:
    print("You achieved Grade D")
    
else:
    print("fail") """
    
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

