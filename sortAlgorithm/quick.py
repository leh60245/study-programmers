def quickSort(data, low, high):
    p = data[(low + high) // 2]  # pivot 선택
    left, right = low, high
    print(p)
    while True:
        while data[left] < p:
            left += 1
        while data[right] > p:
            right -= 1
        if left >= right:
            break
        data[left], data[right] = data[right], data[left]
        print(left, right, data)

    if low < right:
        quickSort(data, low, right)
    if left < high:
        quickSort(data, right + 1, high)


data = [9, 0, 1, 8, 7, 2, 5, 4, 3, 6]
quickSort(data, 0, len(data) - 1)
print(data)
