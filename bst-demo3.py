class BST:
    def __init__(self, data):
        self.data = data
        self.left= None
        self.right = None
    
    def insert(self, data):
        current = self
        while True:
            if data < current.data:
                if current.left is None:
                    current.left = BST(data)
                    return
                current = current.left
            
            if data> current.data:
                if current.right is None:
                    current.right = BST(data)
                    return
                current = current.right
            
    def inorder(self):

        stack = [self]
        
        while stack:
            current = stack.pop()
            print(current.data, " ")
        
            if current.right:
                stack.append(current.right)
            
            if current.left:
                stack.append(current.left)
                
    def find_min(self):
        current = self
        while current.left is not None:
            current= current.left
        return current.data 
    
    def find_max(self):
        current = self
        while current.right is not None:
            current= current.right
        return current.data 
    
    def search(self, x):
        current = self
        
        while current is not None:
            if current.data == x:
                print("value found")
                return 
            elif x < current.data:
                current = current.left
                
            elif x > current.data:
                current = current.right
    
    def delete(self, data):
        
        if data < self.data:
            if self.left:
                self.left = self.left.delete(data)
            return self
            
        if data > self.data:
            if self.right:
                self.right = self.right.delete(data)
            return self
            
        if data == self.data:
            if self.left is None and self.right is None:
                return None
            
            if self.left is None:
                return self.right
            if self.right is None:
                return self.left
            
            if self.left and self.right:
                
                inorder_successor = self.right.find_min()
                self.data = inorder_successor
                self.right = self.right.delete(inorder_successor)
                return self
        
            
       
            
            
                
            

root = BST(50)
root.insert(10)
root.insert(25)
root.insert(100)
root.insert(125)

root.delete(100)
root.inorder()