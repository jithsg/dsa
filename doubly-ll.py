class Node:
    def __init__(self, data):
        self.data = data
        self.nref = None
        self.pref = None
        
class Doublylinkedlist:
    def __init__(self):
        self.head = None
        
    
    def insert_end(self, data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
            return 
        
        current = self.head
        while current.nref is not None:
            current = current.nref
        new_node = Node(data)
        current.nref = new_node
        new_node.pref = current
        
    def insert_begin(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return 
        
        new_node.nref = self.head
        self.head.pref = new_node
        self.head = new_node
        
    def traverse_forward(self):
        if self.head is None:
            print("Doubly Linkedlist is empty")
        
        current = self.head
        while current is not None:
            print(current.data, end = " -> ")
            current = current.nref
    
    def traverse_reverse(self):
        if self.head is None:
            print("Doubly Linkedlist is empty")
            
        current = self.head
        while current.nref is not None:
            current = current.nref
        # print(current.data)
        
        while current is not None:
            print(current.data, end = " <- ")
            current = current.pref
            
        
        
        
    
        
        
dl = Doublylinkedlist()
dl.insert_begin(30)
dl.insert_begin(20)
dl.insert_begin(10)

dl.traverse_reverse()