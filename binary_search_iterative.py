def bs(sorted_array, target, left_pointer, right_pointer):
    while left_pointer<right_pointer:
    
        mid_index = (left_pointer + right_pointer)//2
    
        if target == sorted_array[mid_index]:
            return mid_index
        
        if target < sorted_array[mid_index]:
            right_pointer = mid_index
            
        if target > sorted_array[mid_index]:
            left_pointer = mid_index + 1
            
    return "Not found"
            
        
        
    
    
    
        
    
    