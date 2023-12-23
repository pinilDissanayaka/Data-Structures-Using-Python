class Node(object):
    def __init__(self, data) -> None:
        self.data = data
        self.next = None
        self.prev = None
    
class DoublyLinkedList(object):
    def __init__(self) -> None:
        self._head = None
    
    def insert(self, data):
        newNode = Node(data)
        if(self._head == None):
            self._head = newNode
            newNode.next = None
            newNode.prev = None
        else:
            currNode = self._head
            while(currNode.next != None):
                currNode = currNode.next
            
            currNode.next = newNode
            newNode.prev = currNode
            newNode.next = None
            
    def print(self):
        if(self._head == None):
            print("Doubly linked list is empty...")
            return
        else:
            currNode = self._head
            while(currNode != None):
                print(currNode.data, end= ' ')
                currNode = currNode.next
        