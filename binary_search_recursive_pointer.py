def bs(sorted_array, target, left_pointer, right_pointer):
    if left_pointer > right_pointer:
        return "Not found"
    
    mid_index = (left_pointer + right_pointer)//2
    
    if target == sorted_array[mid_index]:
        return mid_index
    
    if target < sorted_array[mid_index]:
        return bs(sorted_array, target, left_pointer, mid_index)
    
    if target > sorted_array[mid_index]:
        return bs(sorted_array, target, mid_index+1, right_pointer)


print(bs([1, 3, 5, 7, 9], 9, 0, 5))