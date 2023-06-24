from main import generate_data

array = []
array = generate_data(array, 0, 20, 10)
print("before sorting:\n", array)

def selection_sort(array):
    size = len(array)
    min = size-1
    pivot=0
    for pivot in range(pivot, size):
        min=size-1
        for i in range(pivot, size):
            if array[min] > array[i]:
                min = i
        array[min], array[pivot] = array[pivot], array[min]
        print(array)



selection_sort(array)
print("after sorting:\n", array)
