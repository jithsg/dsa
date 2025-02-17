def heapify_down(array, n, index):
    smallest = index
    left = 2*index + 1
    right = 2*index +2
    
    if left < n and array[left] < array[smallest]:
        smallest = left
        
    if right < n and array[right] < array[smallest]:
        smallest = right
        
    if smallest != index:
        array[index],  array[smallest] = array[smallest], array[index]
        heapify_down(array, n, smallest)
        
        
def heapify_up(array, index):
    if index == 0:
        return 
    parent = (index- 1)// 2
    
    if array[parent] > array[index]:
        array[parent], array[index] = array[index] , array[parent]
        heapify_up(array, parent)
        
def delete(array):
    
    array[0] = array[-1]
    array.pop()
    
    if len(array) >0:
        heapify_down(array, len(array), 0)
        

def insert(array, value):
    array.append(value)
    heapify_up(array, len(array)- 1)
    

def heapify(array):
    n= len(array)
    
    for i in range(n//2 -1, -1, -1):
        heapify_down(array, n, i)
    return array