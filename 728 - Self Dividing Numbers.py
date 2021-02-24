# ==============================
#         Information
# ==============================

# Title: 728 - Self Dividing Numbers
# Link: https://leetcode.com/problems/self-dividing-numbers/
# Difficulty: Easy
# Language: Python

# Problem:
# A self-dividing number is a number that is divisible by every digit it contains.

# For example, 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.

# Also, a self-dividing number is not allowed to contain the digit zero.

# Given a lower and upper number bound, output a list of every possible self dividing number, including the bounds if possible.

# Example
# Input: 
# left = 1, right = 22
# Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]

# ==============================
#         Solution
# ==============================


def self_dividing_numbers(left, right):
    num = left
    output = []
    while num <= right:
        quotient, remainder = num, 1
        is_self_dividing = True
        while quotient != 0 and remainder != 0:
            quotient, remainder = divmod(quotient, 10)
            if remainder == 0 or num % remainder != 0:
                is_self_dividing = False
                break
        if is_self_dividing:
            output.append(num)
        num += 1
    return output



left = 1
right = 22
print(self_dividing_numbers(left, right))





