# 1201. Ugly Number III
# Medium

# An ugly number is a positive integer that is divisible by a, b, or c.

# Given four integers n, a, b, and c, return the nth ugly number.

# Example 1:

# Input: n = 3, a = 2, b = 3, c = 5
# Output: 4
# Explanation: The ugly numbers are 2, 3, 4, 5, 6, 8, 9, 10... The 3rd is 4.
# Example 2:

# Input: n = 4, a = 2, b = 3, c = 4
# Output: 6
# Explanation: The ugly numbers are 2, 3, 4, 6, 8, 9, 10, 12... The 4th is 6.
# Example 3:

# Input: n = 5, a = 2, b = 11, c = 13
# Output: 10
# Explanation: The ugly numbers are 2, 4, 6, 8, 10, 11, 12, 13... The 5th is 10.
# Example 4:

# Input: n = 1000000000, a = 2, b = 217983653, c = 336916467
# Output: 1999999984

# Constraints:

# 1 <= n, a, b, c <= 109
# 1 <= a * b * c <= 1018
# It is guaranteed that the result will be in range [1, 2 * 109].
import math
def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        def enough(num) -> bool:
            total = (mid // a) + (mid // b) + (mid // c) - (mid // ab) - (mid // ac) - (mid // bc) + (mid // abc)
            return total >= n
        ab = a * b // math.gcd(a, b)
        ac = a * c // math.gcd(a, c)
        bc = b * c // math.gcd(b, c)
        abc = a * bc // math.gcd(a, bc)
        left, right = 1, 10**10
        while left < right:
            mid = left + (right - left) //2
            if enough(mid):
                right = mid
            else:
                left = mid + 1
        return left

n = int(input())
a = int(input())
b = int(input())
c = int(input())
print(nthUglyNumber(n, a, b, c))