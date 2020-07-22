# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    merged_arr = []

    incrA = 0 # incremented index for array A
    incrB = 0 # incremented index for array B
    
    while incrA < len(arrA) and incrB < len(arrB):
        if arrA[incrA] < arrB[incrB]:
            merged_arr.append(arrA[incrA])
            incrA += 1
        else:
            merged_arr.append(arrB[incrB])
            incrB += 1

    # append remaining once reach end of arrs
    while incrA < len(arrA):
        merged_arr.append(arrA[incrA])
        incrA += 1
    while incrB < len(arrB):
        merged_arr.append(arrB[incrB])
        incrB += 1

    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # single element/empty case
    if len(arr) <= 1:
        return arr

    # define midpoint/pivot    
    mid = (len(arr)//2)
    
    # assign recursive merge_sort to respective halves
    arrA, arrB = merge_sort(arr[mid:]), merge_sort(arr[:mid])
    
    # return merged arrays once recursive calls conclude
    return merge(arrA, arrB)

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    # Your code here
    pass


def merge_sort_in_place(arr, l, r):
    # Your code here
    pass

