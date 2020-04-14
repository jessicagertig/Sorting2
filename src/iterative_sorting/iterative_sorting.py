# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        for j in range(1, len(arr)):
            if j >= smallest_index and arr[j] < arr[smallest_index]:
                smallest_index = j     
                
        # TO-DO: swap
        temp = arr[cur_index]
        arr[cur_index] = arr[smallest_index]
        arr[smallest_index] = temp

    return arr

# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    for i in range(0, len(arr)-1):
        i = 0
        ##had to reset to zero each pass would iterate through all elements
        for j in range(1, len(arr)):
            ##the below if statement performs the bubble for a single pass
            if arr[j-1] > arr[j]:
                temp = arr[j-1]
                arr[j-1] = arr[j]
                arr[j] = temp
                ##the nested loops allow the bubble to occur repeatedly until all swaps have been performed
                
    return arr


# # STRETCH: implement the Count Sort function below
# def count_sort( arr, maximum=-1 ):

#     return arr