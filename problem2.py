def min_operations(arr, k):
    n = len(arr)
    
    remainder = arr[0] % k
    for num in arr:
        if num % k != remainder:
            return -1

    arr = [(num - arr[0]) // k for num in arr]
    
    arr.sort()
    median = arr[n // 2]
    operations = sum(abs(x - median) for x in arr)
    
    return operations
arr = [2, 4, 6, 8, 10]
k = 2
print(min_operations(arr, k))