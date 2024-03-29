# Equilibrium Point 
# Easy Accuracy: 49.32% Submissions: 77572 Points: 2
# Given an array A of n positive numbers. The task is to find the first Equilibium Point in the array. 
# Equilibrium Point in an array is a position such that the sum of elements before it is equal to the sum of elements after it.

# Example 1:

# Input:
# n = 1
# A[] = {1}
# Output: 1
# Explanation: Since its the only 
# element hence its the only equilibrium 
# point. 
# Example 2:

# Input:
# n = 5
# A[] = {1,3,5,2,2}
# Output: 3
# Explanation: For second test case 
# equilibrium point is at position 3 
# as elements before it (1+3) = 
# elements after it (2+2).


# Your Task:
# The task is to complete the function equilibriumPoint() which takes the array and n as input parameters and returns the point of equilibrium. Return -1 if no such point exists.

# Expected Time Complexity: O(n)
# Expected Auxiliary Space: O(1)

# Constraints:
# 1 <= n <= 106
# 1 <= A[i] <= 108

def equilibriumPoint(A, N):
    # Your code here
    if N == 1:
        return 1
    left_sum = 0
    s = sum(A)
    for i in range(N):
        s = s - A[i]
        if s == left_sum:
            return i + 1
        left_sum = left_sum + A[i]
    return -1

N = int(input())
A = [int(ele) for ele in input().split()] [ : N]
print(*(equilibriumPoint(A, N)))