class Graph:
    def __init__(self, size):
        self.size = size
        self.graph = [ [ None for row in range (size)]  for column in range(size)]