# Input numbers
numbers = []

while True:
    try:
        num = int(input("Enter a number: "))
        numbers.append(num)
    except ValueError:
        break
# Sorts numbers from lowest to highest
numbers.sort()
print(numbers)