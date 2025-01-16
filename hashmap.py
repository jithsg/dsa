class Hashmap:
    def __init__(self, size):
        self.hashmap =  [None for item in  range(size)]
        
    def key_to_index(self, key):
        sum=0
        for ch in key:
            sum+= ord(ch)
            
        return sum%len(self.hashmap)
    
    def insert(self, key, val):
        idx = self.key_to_index(key)
        
        self.hashmap[idx]= (key, val)
        
    
    def get(self, key):
        idx = self.key_to_index(key)
        
        if self.hashmap[idx] is not None:
            return self.hashmap[idx][1]
        return None
        
        
        

h = Hashmap(5)

h.insert("India", 'IN')
h.insert("China", 'CN')

print(h.get("India"))


