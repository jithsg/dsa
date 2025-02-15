class BST:
    def __init__(self, data):
        self.data = data
        self.left =None
        self.right=None
        
    def insert_1(self, data):
        if data < self.data:
            if self.left:
                self.left.insert_1(data)
            else:
                self.left= BST(data)
        else:
            if self.right:
                self.right.insert_1(data)
            else:
                self.right = BST(data)
    
    def inorder_1(self):
        stack =[self]
        
        while stack:
            current = stack.pop()
            print(current.data, end= " ")
            
            if current.right:
                stack.append(current.right)
            
            if current.left:
                stack.append(current.left)
                
    def insert_2(self, data):
        current = self
        
        while True:
            if data < current.data:
                if current.left is None:
                    current.left = BST(data)
                    return
                current= current.left
                
            elif data > current.data:
                if current.right is None:
                    current.right = BST(data)
                    return 
                current = current.right
                
    def search_1(self, x):
        current = self
        
        if x == current.data:
            print(f"{x} is present")
            return
        while True:
            if x < current.data and current.left:
                if x == current.left.data:
                    print(f"{x} is present")
                    return 
                current = current.left
                
            elif x > current.data and current.right:
                if x == current.right.data:
                    print(f"{x} is present")
                    return 
                current = current.right
            else:
                print(f"{x} is not present")
                break
            
                
            
                
            
                
                
root = BST(50)
root.insert_1(25)
root.insert_2(100)
root.search_1(50)