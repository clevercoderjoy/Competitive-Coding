# Last Substring in Lexicographical Order
# Hard

# Given a string s, return the last substring of s in lexicographical order.

# Example 1:

# Input: s = "abab"
# Output: "bab"
# Explanation: The substrings are ["a", "ab", "aba", "abab", "b", "ba", "bab"]. The lexicographically maximum substring is "bab".
# Example 2:

# Input: s = "leetcode"
# Output: "tcode"

# Constraints:
# 1 <= s.length <= 4 * 105
# s contains only lowercase English letters.

def lg_order(string):
    maxChar = 'a'
    index = []
    for i in range(len(string)):
        if (string[i] >= maxChar):
            maxChar = string[i]
            index.append(i)
    maxString = ""
    for i in range(len(index)):
        if (string[index[i] : len(string)]) > maxString:
            maxString = string[index[i] : len(string)]
    return maxString

string = input()
print(lg_order(string))