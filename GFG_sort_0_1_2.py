def sort_0_1_2(arr,size):
    i = 0
    zero = 0
    two = size - 1
    while i <= two:
        if arr[i] == 0:
            arr[i], arr[zero] = arr[zero], arr[i]
            i += 1
            zero += 1
        if arr[i] == 2:
            arr[i], arr[two] = arr[two], arr[i]
            two -= 1
        else:
            i += 1

size = int(input())
arr = [int(x) for x in input().split()] [ : size]
print(sort_0_1_2(arr, size))