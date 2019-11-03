# Write a function that counts the number of times a specific digit
# occurs in a range (inclusive). The function will look like
#
# Examples
# digit_occurrences(51, 55, 5) ➞ 6
# # [51, 52, 53, 54, 55] : 5 occurs 6 times
#
# digit_occurrences(1, 8, 9) ➞ 0
#
# digit_occurrences(-8, -1, 8) ➞ 1
#
# digit_occurrences(71, 77, 2) ➞ 1


def digit_occurrences(start, end, digit):

    string = ''.join([str(num) for num in range(start, end + 1)])

    return string.count(str(digit))

print(digit_occurrences(51, 55, 5) == 6)
print(digit_occurrences(-8, -1, 8) == 1)
print(digit_occurrences(71, 77, 2) == 1)