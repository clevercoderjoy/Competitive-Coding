# 1=>

# # Ref link: https://www.youtube.com/watch?v=0DnG0Kc9M2E

# def diagonal_matrix_traversal(mat, rows, cols):
#     if not mat or not mat[0]:
#         return []
#     diagonals = [[] for i in range(rows + cols - 1)]
#     for i in range(rows):
#         for j in range(cols):
#             diagonals[i + j].append(mat[i][j])
#     res = diagonals[0]
#     for i in range(1, len(diagonals)):
#         if i % 2 != 0:
#             res.extend(diagonals[i])
#         else:
#             res.extend(diagonals[i][ : : -1])
#     return res

# rows = int(input())
# cols = int(input())
# arr = [[int(i) for i in input().split()] [ : rows] for j in range(cols)]
# print(*(diagonal_matrix_traversal(arr, rows, cols)))

# 2=>

## Last Substring in Lexicographical Order
## Hard

## Given a string s, return the last substring of s in lexicographical order.

## Example 1:

## Input: s = "abab"
## Output: "bab"
## Explanation: The substrings are ["a", "ab", "aba", "abab", "b", "ba", "bab"]. The lexicographically maximum substring is "bab".
## Example 2:

## Input: s = "leetcode"
## Output: "tcode"

## Constraints:
## 1 <= s.length <= 4 * 105
## s contains only lowercase English letters.

# def lg_order(string):
#     maxChar = 'a'
#     index = []
#     for i in range(len(string)):
#         if (string[i] >= maxChar):
#             maxChar = string[i]
#             index.append(i)
#     maxString = ""
#     for i in range(len(index)):
#         if (string[index[i] : len(string)]) > maxString:
#             maxString = string[index[i] : len(string)]
#     return maxString

# string = input()
# print(lg_order(string))

# 3=>

# # First Missing Positive
# # Difficulty: EASY
# # Avg. time to solve
# # 18 min

# # Problem Statement
# # You are given an array of integers of length N, find the first missing positive integer in linear time and constant space.
# # In other words, find the lowest positive integer that does not exist in the array. The array can negative numbers as well.
# # For example, the input [3, 4, -1, 1] should give output 2 because it is the smallest positive number that is missing in the input array.
# # Input Format:
# # The first line of input contains a single integer T, representing the number of test cases or queries to be run. 
# # Then the T test cases follow.

# # The first line of each test case contains a positive integer N which represents the length of the array.

# # The Second line of each test case contains N integers representing the elements of the array.
# # Output Format :
# # For each test case, return the minimum positive integer that is missing from the given input array.
# # Note:
# # You do not need to print anything. It has already been taken care of.
# # Constraint :
# # 1 <= T <= 10
# # 1 <= N <= 10^5
# # -10^5 <= arr[i] <= 10^5

# # Time Limit: 1 sec
# # Sample Input 1 :
# # 1
# # 5
# # 3 2 -6 1 0
# # Sample Output 1:
# # 4
# # Explanation For Input 1:
# # The first positive number is 1 and it is present in the array similarly 2 and 3 are also present in the array.
# # 4 is missing from the array. Thus, the minimum positive integer that is missing is 4.
# # Sample Input 2 :
# # 1
# # 5
# # 0 1 2 3 4
# # Sample Output 2:
# # 5

# def firstMissing(arr):
#     arr.sort()
#     maxValue = max(arr)
#     d = {}
#     for i in range(1, maxValue + 1):
#         d[i] = d.get(i, 0)
#     for i in arr:
#         if i > 0:
#             d[i]=d.get(i, 0) + 1
#     for i in d:
#         if d[i] == 0:
#             return i
#     return maxValue + 1

# size = int(input())
# arr = [int(i) for i in input().split()] [ : size]
# print(firstMissing(arr))


import random

print(random.randint(1,2))