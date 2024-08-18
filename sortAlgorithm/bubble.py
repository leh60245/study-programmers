def bubbleSort(data):
    for i in range(len(data)-1):
        # i = 0 : j = [0, 1, ... , len(data) - 3, len(data) - 2]
        # i = 1 : j = [0, 1, ... , len(data) - 3]
        # ...
        # i = len(data) - 2 : j = [len(data) - 2]
        for j in range(i,len(data)-1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
               
data = [9,0,1,8,7,2,5,4,3,6] 
bubbleSort(data)
print(data)