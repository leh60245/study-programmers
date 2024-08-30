
def rotate_90(sy, sx, length):
    global arr, new_arr
    for y in range(sy, sy + length):
        for x in range(sx, sx + length):
            oy, ox = y - sy, x - sx
            ry, rx = ox, length - oy - 1
            new_arr[sy + ry][sx + rx] = arr[y][x]

    for y in range(sy, sy + length):
        for x in range(sx, sx + length):
            arr[y][x] = new_arr[y][x]
            print(arr[y][x])


arr = [[7 * j + i for i in range(1, 8)] for j in range(7)]
new_arr = [[0] * 7 for _ in range(7)]
sy, sx = 2, 2   # 좌상단 좌표
length = 3      # 돌릴 사각형의 길이

rotate_90(sy, sx, length)

for i in range(len(arr)):
    print(arr[i])