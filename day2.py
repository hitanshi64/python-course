# Variables
name = "Hitanshi"
age = 21
is_student = True

# Print Variables
print("Name:", name)
print("Age:", age)
print("Student:", is_student)

print("\n----- Data Types -----")
print(type(name))
print(type(age))
print(type(is_student))

print("\n----- Arithmetic Operators -----")
a = 10
b = 5

# Addition
print("Addition:", a + b)

# Subtraction
print("Subtraction:", a - b)

# Multiplication
print("Multiplication:", a * b)

# Division
print("Division:", a / b)


# Floor Division
print("Floor Division:", a // b)

# Modulus
print("Modulus:", a % b)

# Power
print("Power:", a ** b)


# Problem 1 solution
name = "Raj"
age = 20
height = 175.5
is_student = True

print(f"Name: {name}", "->", type(name))
print(f"Age: {age}", "->", type(age))
print(f"Height: {height} cm", "->", type(height))
print(f"Is Student: {is_student}", "->", type(is_student))

# Problem 2 solution

print("-------BILL---------")
notebook=40
print("NOTEBOOK=", notebook)
pen= 20
print("PEN=",pen)
bag = 400
print("BAG=", bag)
print("-----------------------")
subtotal = notebook+pen+bag
print("SUBTOTAL=",subtotal)
gst= subtotal*18
print("GST=",gst)
total= subtotal+gst
print("TOTAL=",total)

# Problem 3 solution

a=10
b=20

print("-----before swapping------")
print("a=",a)
print("b=",b)

a,b=b,a

print("------after swapping------")
print("a=",a)
print("b=",b)


print("are a & b is equals??")
print(a == b)