#if statement

age = 21

if age >= 18:
    print("you can vote")

#if-else statement
age=16
if age >=18:
    print("you can vote")
else:
    print("you cannot vote")



#ifelifelse statement

marks = 80
if marks >= 90:
    print("grade A")
elif marks >= 80:
    print("grade B")
elif marks >= 70:
    print("grade C")
else:
    print("fail")


#comparison operators

a = 10
b = 20
print(a ==  b)
print(a != b)
print(a < b)

#logical operator

age = 20
citizen = True

if age >= 18 and citizen:
    print("eligible")


age = 16
special_permission = True

if age >= 18 or special_permission:
    print("Allowed")

is_banned = False

if not is_banned:
    print("Access Granted")

#Problem 1 - Grade Calculator
marks = int(input("Enter your marks: "))

if marks >= 90:
    print("Grade A")
elif marks >= 70:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Fail")

#Problem 2 - Login Checker
username=input("enter username: ")
password=input("enter password: ")

if username == "admin" and password == "1234":
    print("login successfully")
else:
    print("invalid username and password")

#Practice Problem 1 Even or Odd Number

num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even")
else:
    print("Odd")

#Practice Problem 2 Largest of Two Numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a > b:
    print("Largest =", a)
else:
    print("Largest =", b)

#Practice Problem 3 Age Checker
age = int(input("Enter age: "))

if age >= 18:
    print("Adult")
else:
    print("Minor")