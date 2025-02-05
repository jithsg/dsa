def heapify_down(arr, n, index):
    smallest = index
    left = 2*index + 1
    right = 2*index + 2
    
    if left < n and arr[left] < arr[smallest]:
        smallest = left
    
    if right < n and arr[right] < arr[smallest]:
        smallest = right
        
    
    if smallest != index:
        arr[index], arr[smallest] = arr[smallest], arr[index]
        heapify_down(arr, n, smallest)
        
def heapify_up(arr, index):
    
    parent = (index - 1)//2
    
    while index >0 and arr[parent] > arr[index]:
        arr[parent], arr[index] = arr[index], arr[parent]
        index = parent
        parent = (index - 1)//2

def insert(arr, value):
    arr.append(value)
    heapify_up(arr, len(arr)-1)
    
    

def delete(arr, index):
    
    arr[index]= arr[-1]
    arr.pop()
    heapify_down(arr, len(arr), index)
    
    
def heapify(arr):
    n = len(arr)
    # Start from last non-leaf node (n//2 - 1) and move up to root
    for i in range(n//2 - 1, -1, -1):
        heapify_down(arr, n, i)
    return arr

def heapsort(arr):
    n= len(arr)
    
    for i in range(n//2-1, -1, -1):
        heapify_down(arr, len(arr), i)
        
    for i in range(n-1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify_down(arr, i, 0)
    return arr
    
# arr = [1, 3, 6, 5, 9, 8, 10]
arr=[10, 5, 8, 3, 1, 9, 4]

print(heapsort(arr))
# print("Original array:", arr)
# print("After heapify:", heapify(arr))


    
    
        

        
    
    
        
    