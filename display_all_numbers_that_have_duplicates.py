# input 10 numbers
numbers = []
duplicate_numbers = set()

for i in range(10):
    num = int(input("Enter a number: "))
    numbers.append(num)

# checks numbers for duplicates
for num in numbers:    
    if numbers.count(num) > 1:
        duplicate_numbers.add(num)

# displays numbers that have duplicates
print(duplicate_numbers)