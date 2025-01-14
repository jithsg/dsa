class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
    def set_next(self,node):
        self.next =node


class Linkedlist:
    def __init__(self):
        self.head= None
        
    def __iter__(self):
        node = self.head
        
        while node is not None:
            yield node
            node = node.next
            
    def add_to_tail(self, node):
        if self.head is None:
            self.head = node
        
        for curr_node in self:
            last_node= curr_node
            
        last_node.set_next(node)
    
    def add_to_head(self, node):
        if self.head is None:
            self.head = node
        
        node.next = self.head
        self.head = node
        
        



n1 =  Node(10)
n2= Node(20)
n3= Node(30)

l= Linkedlist()

l.head= n1

n1.set_next(n2)

n2.set_next(n3)
n0 =Node(0)

l.add_to_head(n0)

for item in l:
    print(item.data)