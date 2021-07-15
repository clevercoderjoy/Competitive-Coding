def kSmallest(arr, size, k):
    if size == 0:
        return None
    elif size == 1:
        return arr[0]
    arr.sort()
    return arr[k - 1]

size = int(input())
arr = [int(x) for x in input().split()] [ : size]
k = int(input())
print(kSmallest(arr, size, k))