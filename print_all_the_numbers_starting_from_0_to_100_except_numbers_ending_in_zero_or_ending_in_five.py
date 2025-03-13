# print_all_the_numbers_starting_from_0_to_100_except_numbers_ending_in_zero_or_ending_in_five
num = 0
while num <= 100:
    if num % 10 != 0 and num % 10 != 5:
        print(num)
    num += 1