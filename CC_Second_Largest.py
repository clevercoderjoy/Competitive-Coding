# Second Largest Problem Code: FLOW017

# Three numbers A, B and C are the inputs. Write a program to find second largest among them.

# Input
# The first line contains an integer T, the total number of testcases. Then T lines follow, each line contains three integers A, B and C.

# Output
# For each test case, display the second largest among A, B and C, in a new line.

# Constraints
# 1 ≤ T ≤ 1000
# 1 ≤ A,B,C ≤ 1000000
# Example
# Input
# 3 
# 120 11 400
# 10213 312 10
# 10 3 450

# Output

# 120
# 312
# 10

# cook your dish here
try:
    t = int(input())
    for i in range(t):
        arr = [int(element) for element in input().split()] [ : 3]
        a = arr[0]
        b = arr[1]
        c = arr[2]
        largest = a
        second_largest = 0
        if a > b and a > c:
            largest = a
            if b > c:
                second_largest = b
            else:
                second_largest = c
        elif b > a and b > c:
            largest = b
            if a > c:
                second_largest = a
            else:
                second_largest = c
        elif c > b and c > a:
            largest = c
            if b > a:
                second_largest = b
            else:
                second_largest = a
        print(second_largest)
except:
    pass
