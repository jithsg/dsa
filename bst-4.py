class BST:
    def __init__(self, value):
        self.value= value
        self.left= None
        self.right = None
    
    def find_max(self):
        if self.right is None:
            return self.value
        return self.right.find_max()
    
    def find_min(self):
        if self.left is None:
            return self.value
        return self.left.find_min()

    
    def insert(self, value):
        if value < self.value:
            if self.left:
                self.left.insert(value)
            else:
                self.left = BST(value)
        else:
            if self.right:
                self.right.insert(value)
            else:
                self.right = BST(value)
                
    def inorder(self):
        if self.left:
            self.left.inorder() 
        print(self.value)
        
        if self.right:
            self.right.inorder() 
            
    
    
    def delete(self, value):
        if value < self.value:
            if self.left:
                self.left = self.left.delete(value)
        elif  value > self.value:
            if self.right:
                self.right = self.right.delete(value)
        elif value == self.value:
            if self.left is None and self.right is None:
                return None
            elif self.left is None:
                return self.right
            elif self.right is None:
                return self.left
            elif self.left and self.right:
                inorder_successor = self.right.find_min()
                self.value = inorder_successor
                self.right= self.right.delete(inorder_successor)
        return self
            





b= BST(10)
b.insert(6)
b.insert(15)
b.insert(3)
b.insert(7)
b.insert(1)


b.delete(1)
b.inorder()