class BSTNode:
    def __init__(self, data):
        self.left= None
        self.right= None
        self.val= data
        
    
    def insert(self, val):
        if not self.val:
            self.val = val
            return
        
        if val == self.val:
            return
        
        if val < self.val:
            if self.left:
                self.left.insert(val)
                return 
            
            self.left=BSTNode(val)
            return 
    
        if self.right:
                self.right.insert(val)
                return 
        self.right= BSTNode(val)
        return 
        
    def find_min(self):
        current = self
        while current.left is not None:
            current = current.left
        return current.data
            