def bs(sorted_array, target):
    if not sorted_array:
        return None
    
    mid=len(sorted_array)//2
    
    mid_value = sorted_array[mid]
    
    if target == mid_value:
        return mid
    
    if target < mid_value:
        return bs(sorted_array[0:mid], target)
    
    if target > mid_value:
        result = bs(sorted_array[mid+1:], target)
        if result is None:
            return None
        return result + mid + 1
print(bs([1, 3, 5, 7, 9], 9))