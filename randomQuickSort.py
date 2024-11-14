import random
import time

# Randomized partition function
def randomized_partition(arr, low, high):
    pivot_index = random.randint(low, high)
    arr[low], arr[pivot_index] = arr[pivot_index], arr[low]
    
    pivot = arr[low]
    i = low
    for j in range(low + 1, high + 1):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[low], arr[i] = arr[i], arr[low]
    return i

# Randomized Quicksort function
def randomized_quicksort(arr, low, high):
    if low < high:
        pi = randomized_partition(arr, low, high)
        randomized_quicksort(arr, low, pi - 1)
        randomized_quicksort(arr, pi + 1, high)

# Function to run and time the randomized quicksort on different types of arrays
def run_randomized_comparison(arr_type):
    if arr_type == "random":
        arr = random.sample(range(1, 10001), 10000)
    elif arr_type == "sorted":
        arr = list(range(1, 10001))
    elif arr_type == "reversed":
        arr = list(range(10000, 0, -1))

    arr_randomized = arr.copy()
    start_time = time.time()
    randomized_quicksort(arr_randomized, 0, len(arr_randomized) - 1)
    randomized_time = time.time() - start_time

    return randomized_time

array_types = ["random", "sorted", "reversed"]
for arr_type in array_types:
    randomized_time = run_randomized_comparison(arr_type)
    print(f"{arr_type.capitalize()} array:")
    print(f"Randomized Quicksort Time: {randomized_time:.6f} seconds")
    print("-" * 50)
