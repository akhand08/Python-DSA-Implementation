
def selection_sort(array, arr_size):
    for i in range(0, arr_size):
        small_val_indx = i
        
        for j in range(i+1, arr_size):
            if(array[j] < array[small_val_indx]):
                small_val_indx = j
                
        
        if(small_val_indx != i):
            temp = array[small_val_indx]
            array[small_val_indx] = array[i]
            array[i] = temp
            
            
            
def printArray(array):
    print(" ".join(f"{val}" for val in array) )
            
            
            
        
array = [10, 20, 30, 100, 25, 1, 1000, 99, 8, 11]
arr_size = len(array)

print("Array before Selection Sort")
printArray(array)


selection_sort(array, arr_size)
print("Array after Selection Sort")
printArray(array)




        
        