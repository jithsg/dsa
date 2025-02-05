
def min_heapify(arr, n, i):
    smallest = i
    left = 2*i + 1
    right = 2*i + 2
    
    if left < n and arr[left] < arr[smallest]:
        smallest = left
    
    if right < n  and arr[right] < arr[smallest]:
        smallest = right
        
    if smallest != i:
        arr[i], arr[smallest] = arr[smallest], arr[i]
        min_heapify(arr, n, smallest)
        
def build_min_heap(arr):
    n = len(arr)
    # Start heapifying from the last non-leaf node and move up
    for i in range(n // 2 - 1, -1, -1):
        min_heapify(arr, n, i)
        
        
def insert_heap(arr, value):
    arr.append(value)
    i= len(arr) - 1
    
    while i > 0 and arr[(i-1)/2] > arr[i]:
        arr[(i-1)/2], arr[i] = arr[i], arr[(i-1)/2]
        i = (i-1)//2
        
def remove_min(arr):
    if len(arr) == 0:
        return None
    
    root = arr[0]
    arr[0] = arr[-1]
    root.pop()
    
    min_heapify(arr, len(arr), 0)
        
        
arr =[5, 15, 10, 20, 30, 25]
insert_heap(arr, 0)
        
    