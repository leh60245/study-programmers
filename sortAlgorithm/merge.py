def merge(left, right):
    result = list()
    while len(left) > 0 and len(right) > 0:
        if left[0] <= right[0]:
            result.append(left[0])
            left = left[1:]
        else:
            result.append(right[0])
            right = right[1:]

    result.extend([*left, *right])
    print(result)
    return result


def mergeSort(data):
    if len(data) <= 1:
        return data
    mid = len(data) // 2
    left = mergeSort(data[:mid])
    right = mergeSort(data[mid:])
    print(left, right)
    return merge(left, right)


data = [9, 0, 1, 8, 7, 2, 5, 4, 3, 6]
print(mergeSort(data))
