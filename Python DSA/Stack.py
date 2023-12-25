class Stack(object):
    def __init__(self, size) -> None:
        self._top = -1
        self._size = size
        self._arr = list()
        
    def insert(self, data) -> None:
        if(self._top >= self._size):
            print("Stack overflow...")
            return
        else:
            self._top += 1
            self._arr.append(data)
    
    def pop(self, data):
        if(self._top == -1):
            print("Stack is empty..")
            return
        else:
            popElement = self._arr[self._top]
            self._top -= 1
            return popElement
        
    def print(self):
        if(self._top == -1):
            print("Stack is empty..")
            return
        else:
            for i in range(0, self._top):
                print(self._arr[i], end=" ")
    
    def isEmpty(self):
        if(self._top == -1):
            print("Stack is empty..")
            return
        else:
            print("Stack is not empty..")
            return
    
    def size(self):
        if(self._top == -1):
            return 0
        else:
            return (self._top + 1)
        
        
st = Stack(2)


st.insert(10)
st.insert(20)

print(st.size())



