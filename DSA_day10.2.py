arr = [10, 20, 30, 40, 50]
key = int(input("Enter element to find index: "))
if key in arr:
    print("Index:", arr.index(key))
else:
    print("Element not found")