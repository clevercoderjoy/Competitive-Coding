# Majority Element 
# Easy
# Given an array A of N elements. Find the majority element in the array.
# A majority element in an array A of size N is an element that appears more than N/2 times in the array.

# Example 1:

# Input:
# N = 3 
# A[] = {1,2,3} 
# Output:
# -1
# Explanation:
# Since, each element in 
# {1,2,3} appears only once so there 
# is no majority element.
# Example 2:

# Input:
# N = 5 
# A[] = {3,1,3,3,2} 
# Output:
# 3
# Explanation:
# Since, 3 is present more
# than N/2 times, so it is 
# the majority element.

# Your Task:
# The task is to complete the function majorityElement() which returns the majority element in the array. If no majority exists, return -1.

# Expected Time Complexity: O(N).
# Expected Auxiliary Space: O(1).

# Constraints:
# 1 <= N <= 107
# 0 <= Ai <= 106
class Solution:
    def majorityElement(self, A, N):
            
            majority = {}
            for i in range(N):
                if A[i] in majority:
                    majority[A[i]] += 1
                else:
                    majority[A[i]] = 1
            count = 0
            for key in majority:
                if majority[key] > N // 2:
                    count += 1
                    return key
            if count == 0:
                return -1
            #{ 
#  Driver Code Starts
#Initial Template for Python 3

import math

from sys import stdin


def main():
        T=int(input())
        while(T>0):
            
            N=int(input())

            A=[int(x) for x in input().strip().split()]
            
            
            obj = Solution()
            print(obj.majorityElement(A,N))
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends