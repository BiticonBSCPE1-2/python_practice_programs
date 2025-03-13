# Input a number
unique_numbers = []

while True:
    try:
        num = int(input("Enter a number: "))

# Check if number is unique or duplicate and loops until user enters a non-integer
        if num in unique_numbers:
            print("Duplicate")
        else:
            print("Unique")
            unique_numbers.append(num)
    except ValueError:
        break