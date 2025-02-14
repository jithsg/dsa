class BST:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
    def insert(self, data):
        new_node = BST(data)
        current = self
        
        while True:
            if data < current.data:
                if current.left is None:
                    current.left = new_node
                    return
                current= current.left
                
            if data > current.data:
                if current.right is None:
                    current.right = new_node
                    return
                current = current.right
                
    def preorder(self):
        if self is None:
            return 
        stack = [self]
        
        while stack:
            current =stack.pop()
            print(current.data, end= " ")
            
            if current.right:
                stack.append(current.right)
                
            if current.left:
                stack.append(current.left)
                
    def inorder(self):
        current = self
        stack =[]
        
        while True:
            if current is not None:
                stack.append(current)
                current = current.left
            
            elif stack:
                current = stack.pop()
                print(current.data, end = " ")
                current = current.right
                
            else:
                break
    
    def find_min(self):
        current = self
        
        while current.left is not None:
            current = current.left
            
        return current.data
    
    def find_max(self):
        current = self
        
        while current.right is not None:
            current = current.right
            
        return current.data
    

            
        
                
            
        



root= BST(50)
root.insert(30)
root.insert(70)
root.insert(20)
root.insert(40)
root.insert(60)
root.insert(80)


print(root.find_max())
