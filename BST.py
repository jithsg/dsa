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
        return current.val
    
    
    def find_max(self):
        current = self
        while current.right is not None:
            current = current.right
        return current.val
    
    def delete(self, val):
        
        if self.val is None:
            return None
        
        
        if val < self.val:
            if self.left:
                self.left = self.left.delete(val)
            return self
        
        if val > self.val:
            if self.right:
                self.right = self.right.delete(val)
            return self
        
        if self.left is None:
            return self.right
        
        if self.right is None:
            return self.left
        
        
        successor = self.right
        while successor.left:
            successor = successor.left
        self.val = successor.val
        self.right = self.right.delete(successor.val)
        return self
    
    def pre_order(self):
        if self.val is not None:  # Check if the current node has a value
            print(self.val)  # Print the value of the current node

        if self.left:  # Traverse the left subtree
            self.left.pre_order()

        if self.right:  # Traverse the right subtree
            self.right.pre_order()
    
    def post_order(self):
        
        if self.left:
            self.left.post_order()
            
        if self.right:
            self.right.post_order()
            
        if self.val is not None:
            print(self.val)
            
    def in_order(self):
        if self.left:
            self.left.in_order()
            
        if self.val is not None:
            print(self.val)
            
        if self.right:
            self.right.in_order()
    
    
    
    
        
root=BSTNode(10)
root.insert(6)
root.insert(12)
root.insert(7)
root.insert(11)	
root.in_order()
            