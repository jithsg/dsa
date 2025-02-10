class Node:
    def __init__(self, value):
        self.value = value
        self.ref =None
        
class Linkedlist:
    def __init__(self):
        self.head =None
        
    def traverse(self):
        if self.head is None:
            print("Linkedlist is empty")
        else:
            current = self.head
            while current is not None:
                print(current.value, end=" -> ")
                current = current.ref
    
    def add_begin(self, data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node
    
    def add_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return 
        current = self.head
        while current.ref is not None:
            current = current.ref
        current.ref = new_node
        
    def add_after(self, x, value):
        current = self.head
        
        while current is not None:
            if current.value== x:
                new_node = Node(value)
                new_node.ref = current.ref
                current.ref = new_node
                return
            current = current.ref
            
    def add_before(self, x, value):
        
        if self.head is None:
            print("Linked list is empty")
        
        if self.head.value == x:
            new_node = Node(value)
            new_node.ref = self.head
            self.head = new_node
            return 
        
        current= self.head

        while current.ref is not None:
            if current.ref.value== x:
                new_node = Node(value)
                new_node.ref = current.ref
                current.ref = new_node
                return
            current = current.ref
        

            
        
        
            
        
l= Linkedlist()
l.add_begin(1)
l.add_begin(2)
l.add_begin(3)
l.add_after(3, 4)
l.add_before(1, 0)
l.traverse()