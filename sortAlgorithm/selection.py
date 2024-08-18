def selectionSort(data):
    for i in range(len(data)):
        idx = i
        # i = 0, idx = 0 -> j = [1, 2, ... , len(data) - 1]
        for j in range(i+1, len(data)):
            if data[idx] > data[j]:
                idx = j
        data[i], data[idx] = data[idx], data[i]
            
data = [9,0,1,8,7,2,5,4,3,6] 
selectionSort(data)
print(data)