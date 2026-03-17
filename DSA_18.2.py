# Difference between max and min

arr = [10, 5, 20, 8, 15]

maximum = arr[0]
minimum = arr[0]

for num in arr:
    if num > maximum:
        maximum = num
    if num < minimum:
        minimum = num

difference = maximum - minimum

print("Difference:", difference)