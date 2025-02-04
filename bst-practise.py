class BST:
    def __init__(self, value):
        self.value= value
        self.left = None
        self.right = None
        
    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)
    
    def inorder(self):
        if self.left is not None:
            self.left.inorder()
        print(f"Value {self.value}")
        if self.right is not None:
            self.right.inorder()
            
    def preorder(self):
        print(f"Value {self.value}")
        if self.left is not None:
            self.left.preorder()
        if self.right is not None:
            self.right.preorder()
            
    def postorder(self):
        
        if self.left is not None:
            self.left.postorder()
        if self.right is not None:
            self.right.postorder()
        print(f"Value {self.value}")

    def search(self, value):
        if value == self.value:
            return "Value Present"
        
        if value < self.value:
            if self.left is None:
                return "Not found"
            
            return self.left.search(value)
        elif value > self.value:
            if self.left is None:
                return "Not found"
            return self.right.search(value)
    
    def find_min(self):
        if self.left is None:
            return self.value
        return self.left.find_min()
    
    def delete(self, value):
        if self.value is None:
            return None
        
        if value < self.value:
            if self.left:
                self.left = self.left.delete(value)
        elif value > self.value:
            if self.right:
                self.right= self.right.delete(value)
        else: # self.val = value
            if self.left is None and self.right is None: #no child nodes
                return None
            
            if self.left is None: #one child
                return self.right
            if self.right is None:
                return self.left
            
            min_val = self.right.find_min() #2 child nodes
            self.value = min_val
            self.right = self.right.delete(min_val)
            
        return self
                
        
        
        
    
            
        

           
b= BST(50)
b.insert(100)
b.insert(125)
b.insert(25)
b.insert(10)

print(b.delete(25))
b.inorder()
print(b.delete(125))
b.inorder()