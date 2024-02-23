class HashMap(object):
    def __init__(self, max) -> None:
        self.max=max
        self.hash=[None for i in range(0, max)]
    
    def getHash(self, key):
        for char in key:
            hashedKey=0
            hashedKey =+ ord(char)
            index=hashedKey % self.max
        return index
    
    def getItem(self, key):
        index=self.getHash(key=key)
        value=self.hash[index]
        return value
    
    def setItem(self, key, value):
        index=self.getHash(key=key)
        self.hash[index]=value
        



hashmap= HashMap(10)

hashmap.setItem('A', 102)

print(hashmap.getItem('b'))
        
        