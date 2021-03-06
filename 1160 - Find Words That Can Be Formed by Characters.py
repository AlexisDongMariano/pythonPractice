# ==============================
#         Information
# ==============================

# Title: 53 - Maximum Subarray
# Link: https://leetcode.com/problems/matrix-diagonal-sum/
# Difficulty: Easy
# Language: Python

# Problem:
# Given a square matrix mat, return the sum of the matrix diagonals.

# Only include the sum of all the elements on the primary diagonal and all
# the elements on the secondary diagonal that are not part of the primary diagonal.

# Example
# Input: mat = [[1,2,3],
#               [4,5,6],
#               [7,8,9]]

# Output: 25
# Explanation: Diagonals sum: 1 + 5 + 9 + 3 + 7 = 25
# Notice that element mat[1][1] = 5 is counted only once.

# ==============================
#         Solution
# ==============================

def diagonal_sum(mat):
    length = len(mat)
    l_pointer = 0
    r_pointer = length - 1
    total = 0
    
    for i in range(length):
        if l_pointer == r_pointer:
            total += mat[i][r_pointer]
        else:
            total += mat[i][l_pointer] + mat[i][r_pointer]
        l_pointer += 1
        r_pointer -= 1
        
    return total


def diagonal_sum2(mat):
    n = len(mat)
    n_half = n // 2
    total = 0

    for i in range(n):
        total += mat[i][i]
        total += mat[i][n - 1 - i]

    if n % 2 != 0:
        total -= mat[n_half][n_half]
    
    return total


mat = [[1,2,3],
    [4,5,6],
    [7,8,9]]

mat2 = [[1,1,1,1],
    [1,1,1,1],
    [1,1,1,1],
    [1,1,1,1]]

print(diagonal_sum(mat))
print(diagonal_sum(mat2))
print(diagonal_sum2(mat))
print(diagonal_sum2(mat2))
