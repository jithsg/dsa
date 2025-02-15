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
            

root = BST(50)
root.insert(10)
root.insert(25)
root.insert(100)
root.insert(125)

print(root.find_max())