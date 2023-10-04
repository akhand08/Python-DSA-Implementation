

def bubble_sort(array):
    for i in range(0, len(array)):
        sorted = False
        
        for j in range(0, len(array)-1):
            if array[j] > array[j+1]:
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp
                sorted = True
                
        if sorted == False:
            break
        


array = [43, 21, 10, 56, 34, 78, 90, 15, 27, 69]

print("Array before bubble sort: ")
print( " ".join(f"{val}" for val in array) )

bubble_sort(array)

print("Array after bubble sort: ")
print(" ".join(f"{val}" for val in array))               