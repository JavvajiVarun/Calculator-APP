a = int(input("Enter first number : "))
b = int(input("Enter second number : "))

c = int(input("Enter 1 to add , 2 to subtract , 3 to multiply and 4 to divide "))

if c == 1 :
    print("sum is : " , a+b)
elif c == 2 :
    print("Difference is : " , a-b)
elif c == 3 :
    print("Product is : " , a * b)
elif c == 4 :
    print("Answer : " , a / b)

