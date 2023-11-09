


class QuickSort:


    def median_three_elements(self, a, b, c):
        if a>b:
            if a>c:
                if b>c:
                    return b
                else:
                    return c
            else:
                return a
        else:
            if b>c:
                if a>c:
                    return a
                else:
                    return c
            else:
                return b

    def partition(self, array, type):
        if type == "first": # take first element as pivot
            pivot = array[0] 
        elif type == "last": # take last element as pivot
            pivot = array[len(array)-1] 
            array[0], array[len(array)-1] = array[len(array)-1], array[0]
        else: # median-of-three as pivot
            first = array[0] 
            middle = array[int(len(array)/2)-1] if len(array) % 2 ==0 else array[int(len(array)/2)]
            final = array[len(array)-1]
            pivot = self.median_three_elements(first, middle, final)
            index_pivot = array.index(pivot)
            array[0], array[index_pivot] = array[index_pivot], array[0]

        i = 1
        for j in range(1, len(array)):
            if array[j] < pivot:
                array[i], array[j] = array[j], array[i]
                i+=1

        array[0], array[i-1] = array[i-1], array[0]
        return array, i-1

    def call_quicksort(self, array_numbers, type):

        number_elements = len(array_numbers)
        if number_elements < 2:
            return array_numbers
        else:
            array_partitioned, pos_pivot = self.partition(array_numbers, type)
            right = array_partitioned[0: pos_pivot]
            left = array_partitioned[pos_pivot+1:]
            result_right = self.call_quicksort(right, type)
            result_left = self.call_quicksort(left, type)
            return result_right + [array_partitioned[pos_pivot]] + result_left



if __name__ == "__main__":
    QSORT = QuickSort()
    #ARRAY_NUMBERS = [3, 8, 2, 5, 1, 4, 7, 6]
    ARRAY_NUMBERS =    [4,3,2,5,1]  
    TYPE = "first"
    #print("QUICKSORT pivot first: ", QSORT.call_quicksort(ARRAY_NUMBERS, TYPE))
    TYPE = "last"
    #print("QUICKSORT pivot last: ", QSORT.call_quicksort(ARRAY_NUMBERS, TYPE))
    TYPE = "median-of-three"
    print("QUICKSORT pivot median: ", QSORT.call_quicksort(ARRAY_NUMBERS, TYPE))
