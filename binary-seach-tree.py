class BST:
    def __init__(self, value):
        self.value= value
        self.left= None
        self.right = None
        
    def insert(self, value):
        if value< self.value:
            if self.left is None:
                self.left = BST(value)
            else: 
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)
            
    def minimum(self):
        if self.left is None:
            return self.value
        return self.left.minimum()
    
    def maximum(self):
        if self.right is None:
            return self.value
        return self.right.maximum()
    
    def preorder(self):
        print(self.value)
        if self.left:
            self.left.preorder()
        if self.right:
            self.right.preorder()
    
    def inorder(self):
        if self.left:
            self.left.inorder()
        
        print(self.value)
        
        if self.right:
            self.right.inorder()
            
    def postorder(self):
        if self.left:
            self.left.postorder()
            
        if self.right:
            self.right.postorder()
            
        print(self.value)
        
    def delete(self, value):
        if value < self.value:
            if self.left:
                self.left = self.left.delete(value)
        elif value> self.value:
                self.right = self.right.delete(value)
        
        else:
            if self.left is None and self.right is None:
                return None
            
            elif self.left is None:
                return self.right
                
            elif self.right is None:
                return self.left
                
            elif self.left and self.right:
                inorder_successor  = self.right.minimum()
                self.value = inorder_successor
                self.right = self.right.delete(inorder_successor)
        return self
            
            
b= BST(8)
b.insert(3)
b.insert(10)
b.insert(1)
b.insert(6)
b.insert(7)
b.insert(10)
b.insert(14)
b.insert(13)


b.delete(1)
b.postorder()
