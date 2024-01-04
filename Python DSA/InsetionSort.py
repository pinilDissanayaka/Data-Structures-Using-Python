class InsertionSort(object):
    def insertionSort(arr):
        for i in range(1, len(arr)):
            temp = arr[i]
            j = i - 1
            
            while(j >= 0 and temp >= arr[i]):
                arr[j + 1] = arr[j]
                j = j - 1
                
            arr[j + 1] = temp
            
        return arr