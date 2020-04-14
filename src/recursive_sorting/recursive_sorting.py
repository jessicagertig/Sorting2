arr1 = [2, 7, 5, 1, 9]
                                                 
# TO-DO: complete the helper function below to merge 2 sorted arrays(and )
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    # TO-DO
    i = 0 #pointer for arrA
    j = 0 #pointer for arrB
    k = 0 #pointer for merged_arr
    while k < len(merged_arr):
        if i >= len(arrA):
            merged_arr[k] = arrB[j]
            k+=1
            j+=1
        elif j >= len(arrB):
            merged_arr[k] = arrA[i]
            k+=1
            i+=1
        elif arrA[i] <= arrB[j]:
            merged_arr[k] = arrA[i]
            k+=1
            i+=1
        elif arrA[i] > arrB[j]:
            merged_arr[k] = arrB[j]
            k+=1
            j+=1

    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    if len(arr) <= 1:
        return arr

    mid = len(arr)//2
    arr1 = arr[:mid]
    arr2 = arr[mid:]
    
    arr1 = merge_sort(arr1)
    arr2 = merge_sort(arr2)

    arr = merge(arr1, arr2)

    return arr

print(merge_sort(arr1))


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
