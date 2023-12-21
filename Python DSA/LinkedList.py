class Node(object):
    def __init__(self, data: int) -> None:
        self.data = data
        self.next = None

class LinkedList(object):
    def __init__(self) -> None:
        self._head = None
    
    def insert(self, data):
        newNode = Node(data)
        if(self._head == None):
            self._head = newNode
        else:
            currNode = self._head
            while(currNode.next != None):
                currNode = currNode.next
                
            currNode.next = newNode
            newNode.next = None
            
    def printLinkedList(self):
        currNode = self._head
        while(currNode != None):
            print(currNode.data, end = ' ')
            currNode = currNode.next
            
            
            
            

            
    
    

        
        
        

