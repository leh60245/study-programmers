def insertionSort(data):
    for idx in range(1, len(data)):
        i = idx
        while i > 0 and data[i - 1] > data[i]:
            data[i - 1], data[i] = data[i], data[i - 1]
            i -= 1


data = [9, 0, 1, 8, 7, 2, 5, 4, 3, 6]
insertionSort(data)
print(data)
# idx = 1, i = 1: data = [0,9,1,8,7,2,5,4,3,6]
# idx = 2, i = 2: data = [0,1,9,8,7,2,5,4,3,6]
# idx = 3, i = 3: data = [0,1,8,9,7,2,5,4,3,6]
# idx = 4, i = 4: data = [0,1,8,7,9,2,5,4,3,6], i = 3: data = [0,1,7,8,9,2,5,4,3,6]
# ...
