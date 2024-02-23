class HashMap(object):
    def __init__(self, max) -> None:
        self.max=max
        self.hash=[[] for i in range(0, max)]
    
    def getHash(self, key):
        for char in key:
            hashedKey=0
            hashedKey =+ ord(char)
            index=hashedKey % self.max
        return index
    
    def __getitem__(self, key):
        index=self.getHash(key=key)
        for idx, element in enumerate(self.hash[index]):
            if len(element)==2 and element[0]==key:
                value=self.hash[index][idx][1]
        return value
    
    def __setitem__(self, key, value):
        index=self.getHash(key=key)
        exist=False
        for idx, element in enumerate(self.hash[index]):
            if ((len(element)==2) and (element[0]==key)):
                self.hash[index][idx]=(key, value)
                exist=True
                
                
        if not exist:
            self.hash[index].append((key, value))
        
    def __delitem__(self, key):
        index=self.getHash(key=key)
        for idx, element in enumerate(self.hash[index]):
            if len(element)==2 and element[0]==key:
                self.hash[index][idx]=(None, None)



hashmap= HashMap(10)

hashmap["march 6"] = 310
hashmap["march 7"] = 420
hashmap["march 8"] = 67
hashmap["march 17"] = 6345706

print(hashmap["march 8"])
        
        