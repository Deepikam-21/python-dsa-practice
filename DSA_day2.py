# Reverse an Array
arr = [1, 2, 3, 4, 5]
left = 0
right = len(arr) - 1
while left < right:
    arr[left], arr[right] = arr[right], arr[left]
    left += 1
    right -= 1
print("Reversed array:", arr)

# Find Second Largest Element
arr2 = [10, 20, 4, 45, 99]
largest = second = float('-inf')
for num in arr2:
    if num > largest:
        second = largest
        largest = num
    elif num > second and num != largest:
        second = num
print("Second largest element:", second)