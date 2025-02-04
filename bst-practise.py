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
        
    
            
        

           
b= BST(50)
b.insert(100)
b.insert(125)
b.insert(25)
b.insert(10)

print(b.search(15))