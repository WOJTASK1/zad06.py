from main import generate_data

array = []
array = generate_data(array, 0, 20, 10)
print("before sorting:\n", array)

def merge(left, right):
    merged = []
    i = j = 0

    # Compare elements from both halves and merge them in sorted order
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    # Copy any remaining elements from the left or right halves
    while i < len(left):
        merged.append(left[i])
        i += 1

    while j < len(right):
        merged.append(right[j])
        j += 1

    return merged

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    # Divide the array into two halves
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Recursively sort the two halves
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    # Merge the sorted halves
    merged = merge(left_half, right_half)
    return merged
array=merge_sort(array)
print("after sorting:\n",array)