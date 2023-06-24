from main import generate_data

array = []
array = generate_data(array, 0, 20, 10)
print("before sorting:\n", array)
# def merge(left, right):
#     merged = []
#     i = j = 0
#
#     # Compare elements from both halves and merge them in sorted order
#     while i < len(left) and j < len(right):
#         if left[i] <= right[j]:
#             merged.append(left[i])
#             i += 1
#         else:
#             merged.append(right[j])
#             j += 1
#
#     # Copy any remaining elements from the left or right halves
#     while i < len(left):
#         merged.append(left[i])
#         i += 1
#
#     while j < len(right):
#         merged.append(right[j])
#         j += 1
#
#     return merged
# def quick_sort(array):
#     pivot=len(array)//2
#     if pivot==0:
#         return array
#     print("pivot:",pivot) #=5
#     for i in range(0,pivot):
#         if(array[i]>pivot):
#             for j in range(pivot,len(array)):
#                 if(array[i]<pivot):
#                     array[i], array[j] = array[j], array[i]
#     print(array)
#     left=array[pivot:]
#     right=array[:pivot]
#     quick_sort(left)
#     quick_sort(right)
#     array=merge(left,right)
#     return array
def quicksort(arr):
    print(arr)
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        left = [x for x in arr[1:] if x < pivot]
        right = [x for x in arr[1:] if x >= pivot]
        return quicksort(left) + [pivot] + quicksort(right)

array=quicksort(array)
print("after sorting:\n", array)


