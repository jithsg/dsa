class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None
        

class Linkedlist:
    def __init__(self):
        self.head = None
        
    def add_begin(self, data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node
    
    def traverse(self):
        if self.head is None:
            print("List is empty")
        current = self.head
        while current is not None:
            print(current.data, end=" -> ")
            current = current.ref
            
    def add_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
            
        current = self.head
        while current.ref is not None:
            current = current.ref
  
        current.ref = new_node
        
    def add_after(self, x, data):
        
        new_node = Node(data)
        current = self.head
        
        if self.head is None:
            print("Linked list is empty, cannot add after the given node.")
            return
            
        while current is not None:
            if current.data == x:
                new_node.ref = current.ref
                current.ref = new_node
                return
            current= current.ref
            
    def add_before(self, x, data):
        new_node = Node(data)
        current = self.head
        
        
        if self.head is None:
            print("Linked list is empty, cannot add before the given node.")
            return
        if self.head.data ==x:
            new_node.ref = self.head
            self.head = new_node
            return 
    
        
        while current.ref is not None:
            if current.ref.data == x:
                new_node.ref= current.ref
                current.ref = new_node
                return 
            current = current.ref
        print(f"Node with value {x} not found.")
        
    def delete_begin(self):
        if self.head is None:
            print("Linkedlist is empty")
            return 
        
        self.head = self.head.ref
        
    def delete_last(self):
        if self.head is None:
            print("Linkedlist is empy")
            return
        if self.head.ref is None: #one node
            self.head =None
            return
        current = self.head
        while current.ref.ref is not None:
            current = current.ref
        current.ref= None
                
    def delete_by_value(self, x):
        if self.head is None:
            print("Linkedlist is empy")
            return
        
        if self.head.data== x:
            self.head = self.head.ref
    
        
        current = self.head
        
        while current.ref is not None:
            if current.ref.data == x:
                current.ref = current.ref.ref
            current = current.ref
            
        if current is None:
            print(f"Node with value {x} not found.")
                
    
        
            
            
        
                
ll= Linkedlist()
ll.add_begin(3)
ll.add_begin(2)
ll.add_begin(1)
ll.add_after(3,4)
ll.add_before(1, 0)

ll.delete_by_value(1)
ll.traverse()