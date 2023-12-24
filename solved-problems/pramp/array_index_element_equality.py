"""
Given a sorted array arr of distinct integers, 
write a function indexEqualsValueSearch that returns the lowest index i for which arr[i] == i. 
Return -1 if there is no such index. 
Analyze the time and space complexities of your solution and explain its correctness.
"""


def binary_search(arr, pos, original_arr):
  '''
  Time complexity: O(log n)
  Space complexity: using additional arr, 
                    it will be reduced using iterative approach.
  '''
  # To solve the problem think about subtract positions to the arr and apply binary search to this new array,
  # but without creatingin this new array
  if len(arr) == 0:
    return -1
  middle = len(arr)//2
  # There are 2 criterias to be verified in the base case:
  # 1. element was found
  # 2. it is actually the lowest found
  if (pos + middle) == arr[middle] and ((pos + middle) == 0 or ((pos + middle - 1) > original_arr[pos + middle - 1])):
    return pos + middle
  elif (pos + middle) > arr[middle]:
    # it is required to update the position
    pos += (middle+1)
    return binary_search(arr[middle+1:], pos, original_arr)
  else:
    return binary_search(arr[:middle], pos, original_arr)
    

def index_equals_value_search(arr):
  pos = 0
  original_arr = arr
  return binary_search(arr, pos, original_arr)


# Test cases:

arr = [-8,0,2,5]
assert index_equals_value_search(arr) == 2

arr = [-1,0,3,6]
assert index_equals_value_search(arr) == -1

