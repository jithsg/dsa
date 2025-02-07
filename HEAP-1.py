def heapify_up(arr, index):
    if index == 0:
        return
    parent = (index - 1)//2
        
    if arr[parent] > arr[index]:
        arr[parent], arr[index] = arr[index], arr[parent]
        heapify_up(arr, parent)
        
def insert(arr, val):
    arr.append(val)
    heapify_up(arr, len(arr)-1)
    
    
def heapify_down(arr, n, index):
    smallest = index
    left = 2* index + 1
    right = 2*index + 2
    
    if left < n and arr[left] < arr[smallest]:
        smallest = left
    
    if right < n and arr[right] < arr[smallest]:
        smallest = right
        
    if smallest != index:
        arr[index], arr[smallest] = arr[smallest], arr[index]
        heapify_down(arr, n, smallest)
        
def delete(arr, index):
    arr[index] =arr[-1]
    arr.pop()
    heapify_down(arr, len(arr), index)
    
def heapify(arr):
    n = len(arr)
    
    for i in range(n//2-1, -1, -1):
        heapify_down(arr, len(arr), i)
        
    
# arr = [2, 4, 5, 10, 8]
arr= [10, 8, 5, 4, 2]

# insert(arr, 1)
# print(arr)
# delete(arr, 0)
heapify(arr)
print(arr)
    
        
        