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
            
    def printLinkedList(self)-> None:
        currNode = self._head
        while(currNode != None):
            print(currNode.data, end = ' ')
            currNode = currNode.next
            
    def insertFront(self, data) -> None:
        newNode = Node(data)
        if(self._head == None):
            self._head = newNode
        else:
            newNode.next = self._head
            self._head = newNode
            
    def insertBack(self, data) -> None:
        newNode = Node(data)
        if(self._head == None):
            self._head = newNode
        else:
            currNode = self._head
            while(currNode.next != None):
                currNode = currNode.next
            
            currNode.next = newNode
            newNode.next = None
            
    def removeByPosition(self, position : int) -> None:
        if(position < 0):
            return
        else:
            if(self._head == None):
                print("LinkedList is Empty.")
                return
            else:
                currPosition = 0
                currNode = self._head
                if(position == 0):
                    self._head = self._head.next
                    currNode.data = None
                    currNode.next = None
                    return
                else:
                    while(currPosition < position):
                        currPosition += 1
                        currNode = currNode.next
                    currNode.next = currNode.next.next
                
                
                
                

            
    
            
        
            
            
            
            

            
    
    

        
        
        

