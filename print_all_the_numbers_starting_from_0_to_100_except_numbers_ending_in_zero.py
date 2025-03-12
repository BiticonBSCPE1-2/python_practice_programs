# Prints all numbers from 0 to 100 except numbers ending in zero
for i in range(101):
    if i % 10 != 0:
        print(i)