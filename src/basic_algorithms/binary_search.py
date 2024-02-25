
# Binary search (in ordered arrary)
arr = [1,2,3,4,5,10,20]

def bs(arr, elem):

    middle = len(arr)//2 # works for even or odd elements of array

    if len(arr) == 0: # it is since element to find will be outside of the array
        return False
    else:
        if elem == arr[middle]:
            return True
        else:
            if elem > arr[middle]:
                return bs(arr[middle+1:], elem)
            else:
                return bs(arr[0:middle], elem)
    
print(bs(arr, 4))