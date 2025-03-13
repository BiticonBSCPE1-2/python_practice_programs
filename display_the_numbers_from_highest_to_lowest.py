# input numbers
numbers = []

while True:
    try:
        num = int(input("Enter a number: "))
        numbers.append(num)
    except ValueError:
        break
# sorts and displays numbers from highest to lowest
numbers.sort(reverse=True)
print(numbers)