def swap(arr, start, end):
    arr[start], arr[end] = arr[end], arr[start]

def reverse(arr, start, end):
    while start < end:
        swap(arr, start, end)
        start += 1
        end -= 1

def arrayRotation(arr, size, x):
    if size == 0:
        return
    if x >= size and size != 0:
        x = x % size
    reverse(arr, 0, size - 1)
    reverse(arr, 0, size - x - 1)
    reverse(arr, size -x, size - 1)
    return arr

size = int(input())
arr = [int(_) for _ in input().split()] [ : size]
x = int(input())
print(arrayRotation(arr, size, x))