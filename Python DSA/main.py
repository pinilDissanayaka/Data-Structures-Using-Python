from LinkedList import LinkedList
from Algorithms import Bubblesort, BinarySearch

if __name__ == '__main__':
    li = [1 , 10, 5, 13, 2, 25]
    
    b = Bubblesort()
    
    sortedLi = b.bubbleSort(li)
    
    bs = BinarySearch()
    
    index = bs.binarySearch(sortedLi, 0, len(li) - 1, 10)
    
    if(index == -1):
        print("Element not found")
    else:
        print(f"{sortedLi[index]} in {index} index")
    
    

    

