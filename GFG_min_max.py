def minMax(arr, size):
    if size == 0:
        return None, None
    elif size == 1:
        return arr[0], arr[0]
    minNum = arr[0]
    maxNum = arr[0]
    for i in range(1, size):
        if arr[i] > maxNum:
            maxNum = arr[i]
        if arr[i] < minNum:
            minNum = arr[i]
    return minNum, maxNum

size = int(input())
arr = [int(x) for x in input().split()] [ : size]
print(minMax(arr, size))