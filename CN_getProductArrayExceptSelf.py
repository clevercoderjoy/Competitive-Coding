# Product Of Array Except Self
# Difficulty: EASY
# Avg. time to solve
# 26 min

# Problem Statement
# You have been given an integer array/list (ARR) of size N.
# You have to return an array/list PRODUCT such that PRODUCT[i] is equal to the product of all the elements of ARR except ARR[i]
# Note :
# Each product can cross the integer limits, so we should take modulo of the operation. 

# Take MOD = 10^9 + 7 to always stay in the limits.
# Follow Up :
# Can you try solving the problem in O(1) space?
# Input Format :
# The first line contains an integer 'T' which denotes the number of test cases or queries to be run. Then the test cases follow.

# The first line of each test case or query contains an integer 'N' representing the size of the array/list.

# The second line contains 'N' single space-separated integers representing the elements in the array/list.
# Output Format :
# For each test case, print the elements of the 'PRODUCT' array separated by a single space. 

# Output for every test case will be printed in a separate line.
# Important Note :
# You are required to return the product array and no need to print the result explicitly. It has already been taken care of.
# Constraints :
# 1 <= T <= 100
# 0 <= N <= 10^5
# 0 <= ARR[i] <= 10^5

# Time Limit: 1 sec
# Sample Input 1 :
# 2
# 3
# 1 2 3
# 3
# 5 2 2
# Sample Output 1 :
# 6 3 2
# 4 10 10
# Explanation For Sample Output 1 :
# Test case 1 : Given array = {1, 2, 3] 
# Required array = [2 * 3, 1 * 3, 1 * 2] = [6, 3, 2]
# Test case 2 : Given array = {5, 2, 2] 
#  Required array = [2 * 2, 5 * 2, 5 * 2] = [4, 10, 10]
# Sample Input 2 :
# 2
# 1
# 100
# 2
# 1 2
# Sample Output 2 :
# 1
# 2 1

mod = 10 ** 9 + 7
def getProductArrayExceptSelf(arr, n) :
    output = [1] * n
    product = 1
    for i in range(n):
        
        output[i] = product
        product = (product * arr[i]) % mod
    
    product = 1
    for i in range(n - 1, -1, -1) :
        
        output[i] =(output[i] * product) % mod
        product = (product * arr[i]) % mod

    return output

n = int(input())
arr = [int(x) for x in input().split()]
print(getProductArrayExceptSelf(arr, n))