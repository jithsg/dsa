class BST:
    def __init__(self, value, depth=1):
        self.value = value
        self.depth= depth
        self.left= None
        self.right=None
    
    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value, self.depth+1)
                print(f"Value {value} inserted to left of {self.value} at depth {self.depth+1}")
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value, self.depth+1)
                print(f"Value {value} inserted to right of {self.value} at depth {self.depth+1}")
            else:
                self.right.insert(value)
    def get_node_by_value(self, value):
        if value == self.value:
            return self
        elif value < self.value and self.left:
            return self.left.get_node_by_value(value)
        elif value > self.value and self.right:
            return self.right.get_node_by_value(value)
        else:
            return None
        
    def inorder(self):
        if self.left is not None:
            self.left.inorder()
        print(f'Value {self.value}')
        if self.right is not None:
            self.right.inorder()
            
    def preorder(self):
        print(f'Value {self.value}')
        if self.left is not None:
            self.left.preorder()
        if self.right is not None:
            self.right.preorder()
    
    def postorder(self):
        
        if self.left is not None:
            self.left.postorder()
        if self.right is not None:
            self.right.postorder()
        print(f'Value {self.value}')
        
        
            
                
                
root = BST(100)
root.insert(50)
root.insert(125)
root.insert(75)
root.insert(25)

print(root.get_node_by_value(75).value)

root.postorder()
