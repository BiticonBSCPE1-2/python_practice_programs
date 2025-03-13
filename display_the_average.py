# input numbers
numbers = []

while True:
    try:
        num = int(input("Enter a number: "))
        numbers.append(num)
    except ValueError:
        break

# calculates the average of the numbers
if numbers:
    average = sum(numbers) / len(numbers)
    print(average)
else:
    print("Invalid input")