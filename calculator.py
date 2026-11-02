def add(a, b, d):
    return a + b + d

def subtract(a, b, d):
    return a - b - d

def multiply(a, b, d):
    return a * b * d

def divide(a, b, d):
    return (a / b) / d

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
d = int(input("Enter third number: "))

c = int(input("Enter 1 to add, 2 to subtract, 3 to multiply, 4 to divide: "))

if c == 1:
    print("Sum is:", add(a, b, d))

elif c == 2:
    print("Difference is:", subtract(a, b, d))

elif c == 3:
    print("Product is:", multiply(a, b, d))

elif c == 4:
    print("Answer is:", divide(a, b, d))
