# 1480. Running Sum of 1d Array
# Easy

# Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
# Return the running sum of nums.

# Example 1:
# Input: nums = [1,2,3,4]
# Output: [1,3,6,10]
# Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].

# Example 2:
# Input: nums = [1,1,1,1,1]
# Output: [1,2,3,4,5]
# Explanation: Running sum is obtained as follows: [1, 1+1, 1+1+1, 1+1+1+1, 1+1+1+1+1].

# Example 3:
# Input: nums = [3,1,2,10,1]
# Output: [3,4,6,16,17]

# Constraints:
# 1 <= nums.length <= 1000
# -10^6 <= nums[i] <= 10^6

#snippet already given on the code
#[
class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        #]
        sum = 0
        op = []
        #loop to iterate over the list
        for element in nums:
            #adding each element to the variable sum
            sum += element
            #appending sum to the final output
            op.append(sum)
        #returning the final output
        return op
