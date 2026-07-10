#LEVEL 1

#1
print("hello world")

#2
num1 = int(input("enter num1 "))
num2 = int(input("enter num2 "))
sum = num1 + num2
print(sum)

#3
len = int(input("enter length"))
wid = int(input("enter width"))
area = len * wid
print(area)

#LEVEL 2

#1
num3  = int(input("enter a number"))
if num3>0:
    print("positive")
elif num3<0:
    print("negative")
else :
    print("zero")

#2
year = int(input("enter a year"))
if year%4==0:
    print("leap year")
else :
    print("not a leap year")

#3
grade = int(input("enter a number"))
if grade<=90:
    print("A+")   
elif grade<=80 and grade>90:
    print("A") 
elif grade<=60 and grade>80:
    print("B")       
elif grade<=50 and grade>60:
    print("C")  
else:
    print("F")

#LEVEL 3

#1
for i in range (1,10):
    print(i)

#2
num4 = int(input("enter a number "))
for i in range (1,10):
    print(num4*i)

#LEVEL 6

numbers = [12,13,14,16,15]
largest = numbers[0]
for num in numbers:
    if num > largest:
        largest = num

print(largest)

#LEVEL 7
def factorial(n)
    if n<0 :
        print("invalid num")
        return 0
    if n==1 or n==0:
        return 1
    
result = 1
for i in range(2,n+1):
    result *= i 

return result 

#LEVEL 8

student = {
    "name" : "dd",
    "class" : "5",
    "division" : "D",
    "roll no" : "43",
    "fees status" : "paid"
}
print(student)

#LEVEL 9

file = open("sample.txt","w")
file.write("hello")
file.close()

#LEVEL 10

numer = float(input("enter numerator "))
denom = float(input("enter denominator "))

res = numer/denom
print(res)

except ZeroDivisionError:
    print("cannot be divded by zero")

except ValueError:
    print("invalid format")





    

    