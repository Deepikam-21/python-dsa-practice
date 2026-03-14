# Find maximum element in array

arr = [10, 25, 7, 45, 30]
maximum = arr[0]
for num in arr:
    if num > maximum:
        maximum = num
print("Maximum element:", maximum)