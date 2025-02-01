def hanoi(n, source, destination, intermediate):
    if n==1:
        print(f"Move 1 from {source} to {destination}")
        
        return
    hanoi(n-1, source, intermediate, destination)
    print(f"Move {n} from {source} to {destination}")
    hanoi(n-1, intermediate, destination, source)
    
    
hanoi(4, 'A', 'C', 'B')