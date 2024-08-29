arr = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]

arr_90 = list(map(list, zip(*arr[::-1])))
for i in arr_90:
    for j in i:
        print(j, end=" ")
    print()

print("=======================")

arr_180 = [a[::-1] for a in arr[::-1]]
for i in arr_180:
    for j in i:
        print(j, end=" ")
    print()

print("=======================")

arr_270 = [x[::-1] for x in list(map(list, zip(*arr[::-1])))[::-1]]
for i in arr_270:
    for j in i:
        print(j, end=" ")
    print()
