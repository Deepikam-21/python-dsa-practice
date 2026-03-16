# Count even numbers in array

arr = [4, 7, 10, 13, 18, 21]
count = 0
for num in arr:
    if num % 2 == 0:
        count += 1
print("Even numbers:", count)