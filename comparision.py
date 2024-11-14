import random
import time

# Deterministic Quicksort (fixed pivot - first element)
def deterministic_quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    less_than_pivot = [x for x in arr[1:] if x <= pivot]
    greater_than_pivot = [x for x in arr[1:] if x > pivot]
    return deterministic_quicksort(less_than_pivot) + [pivot] + deterministic_quicksort(greater_than_pivot)

# Randomized Quicksort (random pivot)
def randomized_quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = random.choice(arr)  # randomly select pivot
    less_than_pivot = [x for x in arr if x < pivot]
    greater_than_pivot = [x for x in arr if x > pivot]
    return randomized_quicksort(less_than_pivot) + [pivot] + randomized_quicksort(greater_than_pivot)

# Generate arrays
def generate_arrays(n):
    random_array = random.sample(range(1, n+1), n)
    sorted_array = list(range(1, n+1))
    reverse_sorted_array = sorted_array[::-1]
    return random_array, sorted_array, reverse_sorted_array

# Function to measure and compare execution time
def measure_time(n):
    random_array, sorted_array, reverse_sorted_array = generate_arrays(n)
    
    # Measure time for deterministic Quicksort
    start = time.time()
    deterministic_quicksort(random_array)
    time_deterministic_random = time.time() - start

    start = time.time()
    deterministic_quicksort(sorted_array)
    time_deterministic_sorted = time.time() - start

    start = time.time()
    deterministic_quicksort(reverse_sorted_array)
    time_deterministic_reverse_sorted = time.time() - start

    # Measure time for randomized Quicksort
    start = time.time()
    randomized_quicksort(random_array)
    time_randomized_random = time.time() - start

    start = time.time()
    randomized_quicksort(sorted_array)
    time_randomized_sorted = time.time() - start

    start = time.time()
    randomized_quicksort(reverse_sorted_array)
    time_randomized_reverse_sorted = time.time() - start

    # Print results
    print(f"Array Size: {n}")
    print(f"Deterministic Quicksort (Random Array): {time_deterministic_random:.6f} seconds")
    print(f"Deterministic Quicksort (Sorted Array): {time_deterministic_sorted:.6f} seconds")
    print(f"Deterministic Quicksort (Reverse Sorted Array): {time_deterministic_reverse_sorted:.6f} seconds")
    print(f"Randomized Quicksort (Random Array): {time_randomized_random:.6f} seconds")
    print(f"Randomized Quicksort (Sorted Array): {time_randomized_sorted:.6f} seconds")
    print(f"Randomized Quicksort (Reverse Sorted Array): {time_randomized_reverse_sorted:.6f} seconds")
    print()

# Test with different array sizes
for size in [10, 50, 100]:
    measure_time(size)
