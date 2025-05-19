count = 0
while count < 5:
    print(f"count = {count}")
    count = count + 1
print("Done")

choice = "y"
while choice.lower() == "y":
    print("Hello!")
    choice = input("Say hello again? (Y/N):")
print("Bye!")

count_1 = 0
weight = float(input("Enter the shipment weight: "))
while weight >=10:
    count_1 +=1
    weight = float(input("Enter the shipment weight: "))
print("The count of shipments that are greater than 10 tons is:", count_1)

grade = float(input("Enter your grade? (Enter 0 to end): "))
subjects = 0
sum = 0

while grade < 0:
    grade = float(input("Enter your grade? (Enter 0 to end): "))
    
while grade > 0:
    sum += grade
    subjects +=1
    grade = float(input("Enter your grade? (Enter 0 to end): "))
    
if subjects == 0:
    subjects +=1
    
avg = sum/subjects
print("Your average gardes are: ",avg ) 
 
# another way to do it

grade = float(input("Input grade: "))
count = 0
sum = 0
while grade <= 0:
    print("Please enter VALID number")
    grade =  float(input("Enter your grade?"))
while grade != 0:
    count += 1
    sum += grade
    grade = float(input("Enter your next grade?(Enter 0 to end)"))
average = sum/count
print(average) 


circles = float(input("How many cirles do you want to calculate it for? "))
count = 0
while circles > count:
    count +=1
    area,perimeter = input("Enter the area and perimeter of the circle: ").split(";")
    print(f"The area is {area},The perimeter is {perimeter}")
 

circles = float(input("How many cirles do you want to calculate it for? "))
count = 0
while circles > count:
    count +=1
    radius = float(input("Enter radius: "))
    area = 3.14*(radius**2)
    perimeter = 2*3.14*radius
    print(f"The area is {area},The perimeter is {perimeter}") 
    
students = float(input("Enter the number of students: "))
count = 0
marks = 0
average = 0
while students>count:
    count +=1
    python,networks,math = input("Enter the marks of the three subjects:").split(",")
    mark1 = float(python)
    mark2 = float(networks)
    mark3 = float(math)
    grades = mark1+mark2+mark3
    marks += grades
    average_1 = round(marks/(count*3),2)
    if average_1>90:
        average+=1

print("The average of student:",average_1)
print("Students with average above 90:",average)

