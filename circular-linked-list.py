class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None
        
class CLL:
    def __init__(self):
        self.head = None
        
    def insert_begin(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.head.ref = new_node
            return 
    
       
        
        current = self.head
        while current.ref !=self.head:
            current = current.ref
        new_node.ref = self.head
        current.ref = new_node
        self.head = new_node
        
    def traverse(self):
        if self.head is None:  # Handle empty list case
            print("List is empty")
            return
        current = self.head
        while True:
            print(current.data, end = ' -> ')
            if current.ref == self.head:
                break
            current = current.ref
            
    def insert_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.head.ref = new_node
            return 
        
        current = self.head
        while current.ref != self.head:
            current = current.ref
            
        current.ref = new_node
        new_node.ref= self.head
        
    
    def insert_after(self, x, data):
        if self.head is None:
            print("Circular linked list is empty")
            return 
        
        new_node = Node(data)
        current = self.head
        while current.ref != self.head:
            if current.data == x:
                new_node.ref = current.ref
                current.ref = new_node
                return
            current= current.ref
        if current.data == x:
            current.ref = new_node
            new_node.ref= self.head
            return 
        print(f'{x} is not found')
            
        
            
        
    
    
cl= CLL()
cl.insert_begin(1)
cl.insert_begin(2)
cl.insert_begin(3)
cl.insert_end(4)
cl.insert_after(4, 5)
cl.traverse()


    
            
        