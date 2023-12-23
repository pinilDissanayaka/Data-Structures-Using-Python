class TNode(object):
    def __init__(self, data) -> None:
        self.data = data
        self.LChild = None
        self.RChild = None
        
class Tree(object):
    def __init__(self) -> None:
        self._root = None
        
    def insert(self, node : TNode, data) -> TNode:
        newNode = TNode(data)
        if(self._root == None):
            self._root = newNode
            newNode.LChild = None
            newNode.RChild = None
        else:
            if(node.data > data):
                node.LChild = Tree.insert(self, node.LChild, data)
            elif(node.data < data):
                node.RChild = Tree.insert(self, node.RChild, data)
        return node
    
    def search(self, node : TNode, key) -> TNode:
        if(self._root == None):
            print("Print tree is empty..")
        else:
            if(node.data == key):
                return node
            elif(node.data < key):
                return Tree.search(self, node.RChild, key)
            else:
                return Tree.search(self, node.LChild, key)
            