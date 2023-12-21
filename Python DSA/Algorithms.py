class Bubblesort(object):
    def bubbleSort(self, list_) -> list:
        for i in range(0, len(list_)):
            for j in range (1, (len(list_) - 1)):
                if(list_[j] < list_[j-1]):
                    temp = list_[j]
                    list_[j] = list_[j - 1]
                    list_[j - 1] = temp
        return list_
                
                
class BinarySearch(object):
    def binarySearch(self, list_, first : int, last : int, key) -> list:
        if(last >= first):
            mid = last + first // 2
            if(list_[mid] == key):
                return mid
            elif(key > list_[mid]):
                return BinarySearch.binarySearch(self, list_= list_, first= mid + 1, last= last, key = key)
            else:
                return BinarySearch.binarySearch(self, list_= list_, first= first, last= mid - 1, key = key)
        else:
            return -1
        
        
