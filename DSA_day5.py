# 1. Check if any pair sums to target

arr = [10, 15, 3, 7]
target = 17
seen = set()
found = False
for num in arr:
    if target - num in seen:
        print("Pair found:", num, "and", target - num)
        found = True
        break
    seen.add(num)
if not found:
    print("No pair found")

# 2. Count Occurrences using Hash Map

arr2 = [1, 2, 2, 3, 3, 3, 4]
count = {}
for num in arr2:
    if num in count:
        count[num] += 1
    else:
        count[num] = 1
print("Element frequencies:", count)

# 3. Find Missing Number in Range 1 to N

arr3 = [1, 2, 4, 5]  # Missing 3
n = 5
expected_sum = n * (n + 1) // 2
actual_sum = sum(arr3)
print("Missing number:", expected_sum - actual_sum)