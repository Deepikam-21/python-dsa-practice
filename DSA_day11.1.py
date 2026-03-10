# Find sum of even numbers in array

arr = [2, 5, 8, 11, 14]
sum_even = 0
for num in arr:
    if num % 2 == 0:
        sum_even += num
print("Sum of even numbers:", sum_even)