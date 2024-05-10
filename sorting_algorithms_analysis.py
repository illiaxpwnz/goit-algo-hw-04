import random
import timeit

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
    return arr

def generate_random_list(size):
    return [random.randint(0, 100000) for _ in range(size)]

def measure_sort_time_final(sort_function, size):
    global arr
    arr = generate_random_list(size)
    if sort_function == sorted:
        stmt = "sorted(arr)"
    else:
        stmt = f"{sort_function.__name__}(arr)"
    setup = f"from __main__ import arr"
    if sort_function != sorted:
        setup += f", {sort_function.__name__}"
    return timeit.timeit(stmt, setup=setup, number=5) / 5

sizes = [100, 1000, 5000, 10000]
results = {size: {"insertion_sort": None, "merge_sort": None, "timsort": None} for size in sizes}

for size in sizes:
    results[size]["insertion_sort"] = measure_sort_time_final(insertion_sort, size)
    results[size]["merge_sort"] = measure_sort_time_final(merge_sort, size)
    results[size]["timsort"] = measure_sort_time_final(sorted, size)

print(results)


