# input numbers
highest_number = None

while True:
    try:
        num = int(input("Enter a number: "))
        
# Checks for the highest number
        if highest_number is None or num > highest_number:
            highest_number = num
    except ValueError:
        break

# Displays the highest number
if highest_number is not None:
    print(highest_number)
else:
    print("Invalid input")