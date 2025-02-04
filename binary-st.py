class BST:
    def __init__(self, value, depth=1):
        self.value = value
        self.depth = depth
        self.left = None
        self.right= None
        
    def insert(self, value):
        
        if value < self.value:
            if self.left is None:
                self.left = BST(value, self.depth+1)
                print(f'Tree node {value} added to the left of {self.value} at depth {self.depth + 1}')
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value, self.depth+1)
                print(f'Tree node {value} added to the right of {self.value} at depth {self.depth + 1}')
            else:
                self.right.insert(value)
                
    def get_node_by_value(self, value):
        if self.value == value:
            return self
        
        elif value < self.value and self.left:
            return self.left.get_node_by_value(value)
        
        elif value > self.value and self.right:
            return self.right.get_node_by_value(value)
        else:
            return None
    
    def in_order(self):
        if self.left is not None:
            self.left.in_order()
        print(f'Depth= {self.depth} and Value {self.value}')
        if self.left is not None:
            self.right.in_order()
            
    def maximum(self):
        if self.right is None:
            return self.value
        return self.right.maximum()
    
    def minimum(self):
        if self.left is None:
            return self.value
        return self.left.minimum()
        
        
                
b= BST(100)
b.insert(50)
b.insert(125)
b.insert(25)
b.insert(75)

print(b.maximum())
print(b.minimum())