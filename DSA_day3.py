# 1. Linear Search

arr = [10, 20, 30, 40, 50]
key = 30
for i in range(len(arr)):
    if arr[i] == key:
        print("Element found at index:", i)
        break
else:
    print("Element not found")

# 2. Binary Search (Array must be sorted)

arr2 = [5, 10, 15, 20, 25, 30]
key = 20
low = 0
high = len(arr2) - 1
while low <= high:
    mid = (low + high) // 2
    if arr2[mid] == key:
        print("Element found at index:", mid)
        break
    elif arr2[mid] < key:
        low = mid + 1
    else:
        high = mid - 1
else:
    print("Element not found")