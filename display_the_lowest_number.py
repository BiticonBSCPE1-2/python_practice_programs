# Input a number
lowest_number = None

while True:
    try:
        num = int(input("Enter a number: "))

# Checks the lowest number
        if lowest_number is None or num < lowest_number:
            lowest_number = num
    except ValueError:
        break

# Display the lowest number

if lowest_number is not None:
    print(lowest_number)
else:
    print("Invalid input")