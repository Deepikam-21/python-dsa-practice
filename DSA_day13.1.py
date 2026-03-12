arr = [12, 7, 25, 3, 15]
minimum = arr[0]
for num in arr:
    if num < minimum:
        minimum = num
print("Minimum element:", minimum)