def union(a, n, b, m):
    union = set(a + b)
    return len(union)

n = int(input())
a = [int(x) for x in input().split()] [ : n]
m = int(input())
b = [int(x) for x in input().split()] [ : m]
print(union(a, n, b, m))