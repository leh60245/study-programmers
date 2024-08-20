def binary_search(target, data):
    start = 0
    end = len(data) - 1

    while start < end:
        mid = (end + start) // 2
        if data[mid] == target:
            return mid
        elif target < data[mid]:
            end = mid - 1
        else:
            start = mid + 1

    return None
