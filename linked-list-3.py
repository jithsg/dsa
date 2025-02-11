class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None

class Linkedlist:
    def __init__(self):
        self.head = None
        
    def add_begin(self, data):
        if self.head is None:
            self.head = Node(data)
            return
        
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node
        
    def traverse(self):
        current = self.head
        
        while current is not None:
            print(current.data, end=" -> ")
            current = current.ref
            
    def add_end(self, data):
        if self.head is None:
            self.head= Node(data)
            return
        
        current = self.head
        while current.ref is not None:
            current = current.ref
        current.ref = Node(data)
        
    def add_after(self, x, data):
        if self.head is None:
            print("Linkedlist is empty")
            return
        current = self.head
        while current is not None:
            if current.data == x:
                new_node = Node(data)
                new_node.ref = current.ref
                current.ref = new_node
                return 
            current = current.ref
    
    def add_before(self, x, data):
        if self.head is None:
            print("Linkedlist is empty")
            return
        current = self.head
        
        if self.head.data == x:
            new_node = Node(data)
            new_node.ref = self.head
            self.head = new_node
            return 
            
        while current.ref is not None:
            if current.ref.data == x:
                new_node = Node(data)
                new_node.ref = current.ref
                current.ref = new_node
                return
            current = current.ref
            
        print(f"Node with value {x} not found")
    def delete_begin(self):
        if self.head is None:
            print("Linkedlist is empty")
            return
        self.head = self.head.ref
        
    
    def delete_end(self):
        if self.head is None:
            print("Linkedlist is empty")
            return
        
        if self.head.ref is None:
            self.head = None
            return 
        
        current = self.head
        while current.ref.ref is not None:
            current = current.ref
        current.ref = None
        
    def delete_by_value(self, x):
        if self.head is None:
            print("Linkedlist is empty")
            return
        
        if self.head.data == x:
            self.head = self.head.ref
            return
        
        current = self.head
            
        while current.ref is not None:
            if current.ref.data == x:
                current.ref = current.ref.ref
                return
            current = current.ref
            
        
        print(f"Node with value {x} not found.")
        
                
                
            
        
        
        
            
            
        

ll= Linkedlist()
ll.add_begin(3)
ll.add_begin(2)
ll.add_begin(1)
ll.add_end(4)
ll.add_after(4, 5)
ll.add_before(5, 0)
ll.delete_by_value(1)
ll.traverse()
