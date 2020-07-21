# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    # check if feasible
    if len(arr) == 0:
        return -1
    
    mid = (start + end) // 2

    if arr[mid] == target:
        return mid
    elif target < arr[mid]:
        return binary_search(arr, target, start, mid)
    else:
        return binary_search(arr, target, mid, end)


# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
def agnostic_binary_search(arr, target):
    # check if feasible
    if len(arr) == 0:
        return -1
    lower = 0
    upper = len(arr)-1

    # define ascending condition
    ascending = arr[lower] < arr[upper]
    # while something remains to be sorted/iterated over
    while lower <= upper:
        mid = (lower + upper) // 2

        if arr[mid] == target:
            return mid
        if ascending:

            if target < arr[mid]:
                upper = mid - 1
            else:
                lower = mid + 1
        else:

            if target > arr[mid]:
                upper = mid - 1
            else:
                lower = mid + 1
    
    return -1 