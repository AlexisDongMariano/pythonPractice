# ==============================
#         Information
# ==============================

# Title: 1720 - Decode XORed Array
# Link: https://leetcode.com/problems/decode-xored-array/
# Difficulty: Easy
# Language: Python

# Problem:
# There is a hidden integer array arr that consists of n non-negative integers.
# It was encoded into another integer array encoded of length n - 1, such that 
# encoded[i] = arr[i] XOR arr[i + 1]. For example, if arr = [1,0,2,1], then encoded = [1,2,3].
# You are given the encoded array. You are also given an integer first, that is the
# first element of arr, i.e. arr[0].
# Return the original array arr. It can be proved that the answer exists and is unique.

# Example
    # Input: encoded = [1,2,3], first = 1
    # Output: [1,0,2,1]
    # Explanation: If arr = [1,0,2,1], then first = 1 and encoded = [1 XOR 0, 0 XOR 2, 2 XOR 1] = [1,2,3]

# ==============================
#         Solution
# ==============================


def decode(encoded, first):
    decoded = [first]

    for i in encoded:
        decoded.append(decoded[-1] ^ i)

    return decoded


encoded = [1,2,3]
first = 1

print(decode(encoded, first))