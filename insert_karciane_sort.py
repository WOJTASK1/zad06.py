from main import generate_data
array=[]
array=generate_data(array,0,20,10)
print("before sorting:\n",array)

def insert_sort(array):
    size=len(array)
    pivot=1
    for i in range(size):
        print(array)
        if (array[i] < array[pivot]):
            for j in range(pivot):
                if(array[pivot]>array[j]):
                    array[j], array[pivot] = array[pivot], array[j]
        pivot+=1
        if(pivot==len(array)):
            pivot-=1
insert_sort(array)
print("after sorting:\n",array)