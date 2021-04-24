array1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]

print("Array: ")

for r in array1:
    for c in r:
        print(c, end=" ")
    print()

print("\nDeleted Array: ")

del array1[3]

for r in array1:
    for c in r:
        print(c, end=" ")
    print()