def binary_search(arr, x):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            return mid
    return -1

binary_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
result = binary_search(binary_list, 5)
print(result)