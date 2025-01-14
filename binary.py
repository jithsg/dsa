def binary_search(nums, val):
    if len(nums) <1:
        return False
    
    mid = len(nums)//2
    
    if val == nums[mid]:
        return True
    
    if val < nums[mid]:
        return binary_search(nums[0:mid], val)
    
    if val>nums[mid]:
        return binary_search(nums[mid+1:], val)
    

result= binary_search([0, 1, 4, 5], 5)

if result == True:
    print("present")
else:
    print("absent")       