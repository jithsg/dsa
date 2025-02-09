class queue:
    def __init__(self):
        self.elements= []
        
    def enqueue(self, value):
        self.elements.append(value)
        
    def deque(self):
        return self.elements.pop(0)
        
    