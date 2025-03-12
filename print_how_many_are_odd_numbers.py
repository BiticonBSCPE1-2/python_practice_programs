# Input 10 numbers
count = 0
for i in range(10):
    num = int(input(f"Enter number {i+1}: "))
    if num % 2 != 0:
        count += 1
    else:
        print("It is an even number")

# Prints how many of the numbers are odd
print(count)