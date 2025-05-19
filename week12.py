""" def parameters(purchase,discount,discount_amount,final_bill):
    discount_amount = (discount/100)*purchase
    final_bill = purchase-discount_amount
    return final_bill

def main():
    purchase = float(input("The amount of purchase you made: $"))
    discount = float(input("The discount percent from the store: "))
    discount_amount = (discount/100)*purchase
    final_bill = purchase-discount_amount
    print(f"The purchased amount ${purchase},The discount percentage: {discount}%")
    print(f"The discounted amount: ${discount_amount}")
    print(f"The final amount to be paid: ${final_bill}")
    parameters(purchase,discount,discount_amount,final_bill)
    
if __name__ == "__main__":
    main() """
    
""" def processGrades(grades):
    count = 0
    sum = 0
    countpassing = 0
    while count < grades:
        grade = float(input("Enter a grade: "))
        if grade>=50 and grade <=100:
            sum +=grade
            countpassing += 1
        count +=1
    return sum/countpassing
# return sum,countpassing alternate

def main():
    grades = float(input("Enter the no. of gardes: "))
    passing =  processGrades(grades)
    average = passing
    #average = passing[0]/passing[1] alternate

    print("The average of passing grades is {}".format(average))
    
    
if __name__ == "__main__":
    main()        """
    
""" def changeme(mylist):
    print("Values inside the function before change: ", mylist)
    mylist[2]=300
    print("Values inside the function after change: ", mylist)
    return mylist

def main():
    mylist=[10,20,30,40]
    print("Values outside the function and before making changes: ", mylist)
    changeme(mylist)
    print("Values outside the function and after making changes: ", mylist)

main() """


def final(list_grades,count,total_sum):
    grades = list_grades
    minumum = min(grades)
    maximum = max(grades)
    total = float(total_sum)
    average = total/count
    findings = []
    findings.append(minumum)
    findings.append(maximum)
    findings.append(total)
    findings.append(average)
    return findings

def main():
    list_grades=[]
    count = 0
    total_sum = 0
    while count <= 9:
        grade = float(input("Enter the grade: "))
        if grade>=0 and grade<=100:
            list_grades.append(grade)
            count +=1
            total_sum += grade
    content = final(list_grades,count,total_sum)
    print("The minimum grade:",content[0])
    print("The maximum grade:",content[1])
    print("The sum of all grades:",content[2])
    print("The average grade:",content[3])
            
if __name__ == "__main__":
    main()
