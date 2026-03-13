# Count negative numbers in array

arr = [5, -2, 7, -8, 10, -3]
count = 0
for num in arr:
    if num < 0:
        count += 1
print("Negative numbers:", count)