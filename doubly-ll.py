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
            return
        
        current = self.head
        while current is not None:
            print(current.data, end = " -> ")
            current = current.nref
    
    def traverse_reverse(self):
        if self.head is None:
            print("Doubly Linkedlist is empty")
            return
            
        current = self.head
        while current.nref is not None:
            current = current.nref
        # print(current.data)
        
        while current is not None:
            print(current.data, end = " <- ")
            current = current.pref
            
    def add_after(self, x, data):
        if self.head is None:
            print("Doubly Linkedlist is empty")
            return
        
        current = self.head
        new_node = Node(data)
        while current is not None:
            if current.data == x:
                new_node.nref = current.nref
                new_node.pref = current
                if current.nref is not None:
                    current.nref.pref = new_node
                current.nref= new_node
                return
            current = current.nref
        print(f"Node with value {x} not found in the list.")
        
    
    def add_before(self, x, data):
        if self.head is None:
            print("Doubly Linkedlist is empty")
            return
        new_node = Node(data)
        if self.head.data == x:
            new_node.nref = self.head
            self.head.pref = new_node
            self.head = new_node
            return 
        
        current = self.head
        while current.nref is not None:
            if current.nref.data == x:
                new_node.pref = current
                new_node.nref = current.nref
                current.nref.pref = new_node
                current.nref = new_node
                
                return
            current = current.nref
            
    def delete_begin(self):
        if self.head is None:
            print("Doubly Linkedlist is empty")
            return
        
        if self.head.nref is None:
            self.head = None
            return
            
        self.head = self.head.nref
        self.head.pref = None
        
        
            
            
        
            

    
        
        
dl = Doublylinkedlist()
dl.insert_begin(30)
dl.insert_begin(20)
dl.insert_begin(10)
dl.add_after(30, 40)
dl.add_before(10, 0)



dl.delete_begin()
dl.traverse_forward()