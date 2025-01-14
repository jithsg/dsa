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
            return 
        
        node.next = self.head
        self.head = node
        
    def remove_from_head(self):
        if self.head is None:
            return None
        
        old_head = self.head
        self.head = self.head.next
        old_head.next = None
        return old_head
        
        
        



n1 =  Node(10)
n2= Node(20)
n3= Node(30)

l= Linkedlist()

l.head= n1

n1.set_next(n2)

n2.set_next(n3)
n0 =Node(0)

l.add_to_head(n0)
l.remove_from_head()
l.remove_from_head()

for item in l:
    print(item.data)