def quicksort(arr):
    #base
    if len(arr) <= 1:
        return arr
    
    # Choose the pivot(first element)
    pivot = arr[0]
    
    # Partition the array into two parts: 
    left = []
    right = []
    
    for element in arr[1:]:
        if element <= pivot:
            left.append(element)
        else:
            right.append(element)
    
    # Recursively apply quicksort and combine the sorted parts
    return quicksort(left) + [pivot] + quicksort(right)


arr = [3,1,90,34, 7, 8, 9, 1, 5]
sorted_arr = quicksort(arr)
print("Sorted array:", sorted_arr)
