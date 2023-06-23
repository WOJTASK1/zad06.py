from main import generate_data
array=[]
array=generate_data(array,0,20,10)
print("before sorting:\n",array)
def bubble_sort(array):
    size=len(array)
    for i in range(size):
        for j in range(size-i-1):
            if(array[j]>array[j+1]):
                array[j], array[j+1] = array[j+1], array[j]
bubble_sort(array)
print("after sorting:\n",array)