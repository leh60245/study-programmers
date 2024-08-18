def insertionSort(data):
    for end in range(1, len(data)):
        for j in range(end):
            if data[j] > data[end]:
                data[j], data[end] = data[end], data[j]

data = [9,0,1,8,7,2,5,4,3,6] 
insertionSort(data)
print(data)
# data = [0,9,1,8,7,2,5,4,3,6] 
# data = [0,1,9,8,7,2,5,4,3,6] 
# data = [0,1,8,9,7,2,5,4,3,6] 
# data = [0,1,7,9,8,2,5,4,3,6], [0,1,7,8,9,2,5,4,3,6]
# ...