# input two numbers
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# Prints the numbers between two numbers
if num1 > num2:
    num1, num2 = num1, num2

num1 += 1
while num1 < num2:
    print(num1)
    num1 += 1