

def partition(arr):
    lower = []
    pivot = arr[0]
    upper = []

    
    for x in arr[1:]:
        if x <= pivot: # or equal to is optional
            lower.append(x)
        else:
            upper.append(x)
    return lower, pivot, upper

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    lower, pivot, upper = partition(arr)
    return quicksort(lower) + [pivot] + quicksort(upper)

    # if lower < upper:
    #     # partition index
    #     pi = partition(arr, lower, upper)
    #     quicksort(arr, lower, pi - 1)
    #     quicksort(arr, pi + 1, lower)
    
arr = [13, 27, 5, 18, 3, 19, 22, 16]


print(quicksort(arr))

# for item in tosort:
#     if item < pivot:
#         item goes in left bin
#     else:
#         right bin