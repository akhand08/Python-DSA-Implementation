


            
def printArray(array):
    print("  ".join(f"{val}" for val in array) )
    
    
def merge_sort(array):
    if len(array) >  1:
        
        mid_point = len(array)//2
        left_arr = array[:mid_point]
        right_arr = array[mid_point:]
        
        
        merge_sort(left_arr)
        merge_sort(right_arr)
        
        
        i = j = k = 0
        
        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] <= right_arr[j]:
                array[k] = left_arr[i]
                i += 1
            else:
                array[k] = right_arr[j]
                j += 1
                
            k += 1
            
            
            
        while( i < len(left_arr) ):
            array[k] = left_arr[i]
            i += 1
            k += 1 
            
            
        while( j < len(right_arr) ):
            array[k] = right_arr[j]
            j += 1
            k += 1 
        

    
    
    
    
    
    

if __name__ == '__main__' :
    
    array = [10, 20, 30, 100, 25, 1, 1000, 99, 8, 11]
    
    
    print("Array before Merge Sort: ")
    printArray(array)
    
    
    merge_sort(array)
    
    
    
    print("Array after Merge Sort: ")
    printArray(array)

    