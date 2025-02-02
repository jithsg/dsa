def knapsack(items, n, capacity):
    if n==0 or capacity ==0:
        return 0
    if items[n-1][0] > capacity:
        return knapsack(items, n-1, capacity)
    
    include = items[n-1][1] +knapsack(items, n-1, capacity-items[n-1][0])
    exclude = knapsack(items, n-1, capacity)
    return max(include, exclude)



items = [(2, 3), (3, 4), (4, 5), (5, 6)]  # (weight, value) pairs
capacity = 5
n = len(items)
result = knapsack(items, n, capacity)
print(f"Maximum value: {result}")