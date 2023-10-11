


def insertion_sort(array, arr_size):
    for i in range(1,arr_size):
        key = array[i]
        
        for j in range(i,0,-1):
            if key < array[j-1]:
                array[j] = array[j-1]
                array[j-1] = key
            else:
                array[j] = key
                break
        
            
            
            
            
def printArray(array):
    print("  ".join(f"{val}" for val in array) )
            
            
            
        
array = [10, 20, 30, 100, 25, 1, 1000, 99, 8, 11]
arr_size = len(array)                




print("Array before Insertion Sort: ")
printArray(array)


insertion_sort(array, arr_size)
print("Array after Insertion Sort: ")
printArray(array)
