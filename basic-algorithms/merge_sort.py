#!/bin/python3

'''
This class implement the merge sort algoritm in nlogn
'''

class MergeSort:

    def sort_array(self, arr):
        #print("arr: ", arr)
        if len(arr)<=2:
            if len(arr) == 2:
                if arr[0] > arr[1]:
                    return ([arr[1], arr[0]])
            return (arr)
        
        else:
            div = int(len(arr)/2)-1  if len(arr)%2 == 0 else int(len(arr)/2)
            left = arr[0:div]
            right = arr[div:]
            ordered_left = self.sort_array(left)
            ordered_right = self.sort_array(right)
            ordered = []
            len_final = len(ordered_left) + len(ordered_right)
            i=0
            j=0
            for pos in range(0, len_final):
                if ordered_left[i] > ordered_right[j]:
                    ordered.append(ordered_right[j])
                    j+=1
                else:
                    ordered.append(ordered_left[i])
                    i+=1
                    
                if i == len(ordered_left):
                    ordered = ordered + ordered_right[j:]
                    break
                if j == len(ordered_right):
                    ordered = ordered + ordered_left[i:]
                    break

            print("ordered: ", ordered)
            return ordered

if __name__ == '__main__':

    arr = [5,4,3,2,1]
    #arr = [1,1,1,2,2]
    #arr = [2,1,3,1,2]
    #arr = [1, 2, 1, 2, 1]
    result = MergeSort().sort_array(arr)
    #print(result[1])


