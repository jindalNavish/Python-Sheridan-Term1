""" x = 4
while x>0:
    x -= 1
    if x ==2:
        continue
    print(x)
    
dict_1 = {}
dict_1['ibm'] = '12345'
dict_1['ibm-x'] = '12345-x'
dict_1['hp'] = '45678'
dict_1['asus'] = '56901'
dict_1['lenovo'] = '12345'

search = input('Enter the server code: ')
for server,code in dict_1.items():
    if code == search:
        print(server)
        break
else:
    print("Server does not exist")
print("Thanks!")


print("'How many hi's do you want to print out'")
print("--------------")
 
hi = int(input('Enter the amount of times you want to print hi: '))
hi+=1
while hi <= 0:
    print("Wrong entry try again")
    hi = int(input('Enter the amount of times you want to print hi: '))
    hi += 1
    
for number in range(1,hi):
    print("hi",number, end='!!')
    print()
 
 
list = []
count_1 = 0
for num in range(11):    
    reading = int(input("The reading of the temprature: "))
    if reading<0:
        continue
    count_1+=1        
    list.append(reading)
    if count_1 == 10:
        break
    

print(f"The reading are: {list}")
average = sum(list) / len(list)
print("The average is",average) """

""" cities = {"Brampton":1900 , "Tronto":8000, "Niagra":5000, "Brantford":7000, "Malton":8000 }
var = list(cities.values())
sum = 0


for population in var:
    if population>0:
       sum += population 
    
print("Total population of the cities: ",sum) """

#nested loop
""" for hours in range(24):
    for minutes in range(12):
        for seconds in range(60):
            print(hours,",",minutes,",",seconds,".")
             """
""" for row in range(6):
    for col in range(6):
        print('*', end = ' ')
    print()
    
for r in range(8):
    for c in range(r+1):
        print("*",end=" ")
    print()
   
for i in range(1,6):
    for j in range(1,6):
        if j==3:
            break
        print(i,j)
   """
  
""" avg = []        
for s in range(4):
    total = 0
    for a in range(5):
        grade = int(input("Enter a grade: "))
        total += grade
    average = total/5
    avg.append(grade)
    print("The average of student ",s ,"is", average)
    print()
    print("Continue with next student....")
print(avg) """
      
avg = []       
c = 0
j = 1        
while c<2:
    total = 0
    while j<4:
        grade = int(input("Enter a grade: "))
        total += grade
        j +=1
    average = total/3
    avg.append(grade)
    c +=1
    j = 1
    print("The average of student ",c ,"is", average)
    print()
    print("Continue with next student....")
print(avg)
       