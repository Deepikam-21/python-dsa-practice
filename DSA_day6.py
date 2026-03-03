# 1. Maximum Sum Subarray of Size K (Sliding Window)

arr = [2, 1, 5, 1, 3, 2]
k = 3
window_sum = sum(arr[:k])
max_sum = window_sum
for i in range(k, len(arr)):
    window_sum += arr[i] - arr[i - k]
    max_sum = max(max_sum, window_sum)
print("Maximum sum of subarray of size", k, "is:", max_sum)

# 2. Maximum Subarray Sum (Kadane’s Algorithm)

arr2 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
max_current = arr2[0]
max_global = arr2[0]
for i in range(1, len(arr2)):
    max_current = max(arr2[i], max_current + arr2[i])
    max_global = max(max_global, max_current)
print("Maximum subarray sum:", max_global)