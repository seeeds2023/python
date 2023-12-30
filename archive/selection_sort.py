

def selectionSort(array):
    size = len(arr)
    min_index = 0
    for k in range(size):
        if array[k] < array[min_index]:
            min_index = k
    
    # swapping the elements to sort the array
    temp = array[0]
    array[0] = array[min_index]
    array[min_index] = temp
    print(array)

arr = [-2, 45, 0, 11, -9,88,-97,-202,747]

selectionSort(arr)
print('The array after sorting in Ascending Order by selection sort is:')
# print(arr)