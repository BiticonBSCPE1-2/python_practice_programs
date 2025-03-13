# input numbers
numbers = []
duplicate_numbers = {}

while True:
    try:
        num = int(input("Enter a number: "))
        numbers.append(num)

# Checks for duplicates
        if num in duplicate_numbers:
            duplicate_numbers[num] += 1
        else:
            duplicate_numbers[num] = 1
    except ValueError:
        break

# Outputs the number with the most duplicates
if numbers:
    most_duplicates = max(duplicate_numbers, key=duplicate_numbers.get)
    print(most_duplicates)