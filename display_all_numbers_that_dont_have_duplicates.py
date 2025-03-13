# input 10 numbers
numbers = []
none_duplicate_numbers = []

for i in range(10):
    num = int(input("Enter a number: "))
    numbers.append(num)

# checks numbers for duplicates
for num in numbers:    
    if numbers.count(num) == 1:
        none_duplicate_numbers.append(num)

# displays numbers that don't have duplicates
print(none_duplicate_numbers)