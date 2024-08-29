arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
n = 3

arr_90 = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        arr_90[j][n - i - 1] = arr[i][j]

for i in arr_90:
    for j in i:
        print(j, end=" ")
    print()

print("=======================")

arr_180 = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        arr_180[n - i - 1][n - j - 1] = arr[i][j]

for i in arr_180:
    for j in i:
        print(j, end=" ")
    print()

print("=======================")

arr_270 = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        arr_270[n - j - 1][i] = arr[i][j]


for i in arr_270:
    for j in i:
        print(j, end=" ")
    print()
