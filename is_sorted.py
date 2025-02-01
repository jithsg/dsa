def is_sorted(arr):
    if len(arr) <=1:
        return True
    return arr[0]<=arr[1] and is_sorted(arr[1:])


print(is_sorted([1, 2, 3, 4,6, 5]))