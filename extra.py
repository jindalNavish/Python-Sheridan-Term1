#Question 1
def parameters(purchase,discount,discount_amount,final_bill):
    discount_amount = (discount/100)*purchase
    final_bill = purchase-discount_amount
    return final_bill

def main():
    count = 1
    purchase = float(input("The amount of purchase you made: $"))
    while count > 0:
        discount = float(input("The discount percent from the store: "))
        if discount >0:
            discount_amount = (discount/100)*purchase
            final_bill = purchase-discount_amount
            print(f"The purchased amount ${purchase},The discount percentage: {discount}%")
            print(f"The discounted amount: ${discount_amount}")
            print(f"The final amount to be paid: ${final_bill}")
            parameters(purchase,discount,discount_amount,final_bill)
            count -= 1
        else:
            continue
    
if __name__ == "__main__":
    main() 
    
#Question 2

seconds = int(input("The second you want to countdown from: "))
for countdown in range(seconds):
    if seconds >0:
        print(f"The countdown is {seconds}")
        seconds -= 1
    else:
        print("The countdown is finished") 

#Question 3

lst=[]
sum = 0

n = int(input("No of elements you want in list: "))

for k in range(n):        
    num = int(input("Enter a list of numbers: "))
    if num > 0:
        lst.append(num)
        if num % 2 == 0:
            sum += num 
            
            
print(f"The sum of all even number:{sum}")


#Question 4 

lst_2 = []
student = int(input("Enter the number of students :"))
count = 0

while student>count:
    marks = int(input("Enter the marks of students:"))
    lst_2.append(marks)
    count += 1
    

high = lst_2[0]

for score in lst_2:
    if score >high:
        high = score

print(high)