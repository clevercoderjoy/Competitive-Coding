def reverseList(arr, size):
    for i in range(1, (size // 2) + 1):
        arr[i - 1], arr[-i] = arr[-i], arr[i - 1]
    return arr

size =int(input())
arr = [int(x) for x in input().split()] [ : size]
print(reverseList(arr, size))