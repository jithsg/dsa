
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
        
arr = [10, 20, 5, 15, 30, 25]
build_min_heap(arr)
print("Min-Heap:", arr)
        
        
    