# Sum of odd numbers in array

arr = [3, 6, 9, 12, 15]
sum_odd = 0
for num in arr:
    if num % 2 != 0:
        sum_odd += num
print("Sum of odd numbers:", sum_odd)