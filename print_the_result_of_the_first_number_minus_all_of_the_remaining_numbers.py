# Input 10 numbers
total = 0
for i in range(10):
    num = float(input(f"Enter number {i+1}: "))
    if i == 0:
        total += num
    else:
        total -= num

# Print the value of the first number minus all of the remaining numbers
print(total)