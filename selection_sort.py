from main import generate_data
array=[]
array=generate_data(array,0,20,10)
print("before sorting:\n",array)

def selection_sort(array):
    size=len(array)
    pivot=0
    temp
    for i in range(pivot,size):
        print(array)
        if (array[i] > array[pivot]):
            array[i], array[pivot] = array[pivot], array[i]
    pivot+=1

selection_sort(array)
print("after sorting:\n",array)