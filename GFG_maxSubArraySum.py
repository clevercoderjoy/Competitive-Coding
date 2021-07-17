def maxSubArraySum(arr, size):
    currentMax, maxSoFar = arr[0], arr[0]
    for i in range(1, size):
        currentMax = max(arr[i], currentMax + arr[i])
        maxSoFar = max(maxSoFar, currentMax)
    return maxSoFar

size = int(input())
arr = [int(x) for x in input().split()] [ : size]
print(maxSubArraySum(arr, size))