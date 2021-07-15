def moveNegatives(arr, size):
    if size < 0:
        return None
    elif size == 1:
        return arr[0]
    i, n = 0, 0
    while i < size:
        if arr[i] < 0:
            arr[i], arr[n] = arr[n], arr[i]
            i += 1
            n += 1
        else:
            i += 1
    return arr

size = int(input())
arr = list(map(int, input().split())) [ : size]
print(moveNegatives(arr, size))