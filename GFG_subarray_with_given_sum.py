# Subarray with given sum 
# Easy Accuracy: 39.71% Submissions: 100k+ Points: 2
# Given an unsorted array A of size N that contains only non-negative integers, find a continuous sub-array which adds to a given number S.

# Example 1:

# Input:
# N = 5, S = 12
# A[] = {1,2,3,7,5}
# Output: 2 4
# Explanation: The sum of elements 
# from 2nd position to 4th position 
# is 12.

# Example 2:

# Input:
# N = 10, S = 15
# A[] = {1,2,3,4,5,6,7,8,9,10}
# Output: 1 5
# Explanation: The sum of elements 
# from 1st position to 5th position
# is 15.

# Your Task:
# You don't need to read input or print anything.
# The task is to complete the function subarraySum() which takes arr, N and S as input parameters.
# The function returns a list containing the starting and ending positions of the first such occurring subarray from the left where sum equals to S.
# The two indexes in the list should be according to 1-based indexing. If no such subarray is found, return an array consisting only one element that is -1.

# Expected Time Complexity: O(N)
# Expected Auxiliary Space: O(1)

# Constraints:
# 1 <= N <= 105
# 1 <= Ai <= 1010

# concept of sliding window is used here

def subArraySum(arr, size, x): 
        #Your code here
        start = 0
        end = 1
        curr_sum = arr[0]
        while end <= size:
            while curr_sum > x:
                curr_sum = curr_sum - arr[start]
                start += 1
            if curr_sum == x:
                return start + 1, end
            if end < size:
                curr_sum += arr[end]
            end += 1
        return -1

size = int(input())
arr = [int(element) for element in input().split()] [ : size]
x = int(input())
print(subArraySum(arr, size, x))
