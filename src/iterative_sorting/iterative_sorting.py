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

####Brady's Solution Code for Selection Sort
# def selection_sort(arr):
#     for i in range(0, len(arr) - 1):
#         print(arr)
#         cur_index = i
#         smallest_index = cur_index
#         for j in range(cur_index, len(arr)):
############# 
#By using cur_index as the first parameter in range he eliminate the need for the "j >= smallest_index in my code above"
#############
#             if arr[j] < arr[smallest_index]:
#                 smallest_index = j
# ​
#         arr[smallest_index], arr[cur_index] = arr[cur_index], arr[smallest_index]
############
#above is the elegent way to swap in python, can't believe I forgot this
############
#     return arr

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

########################
#Greg's Solution Code for Bubble Sort:
# def bubble_sort(arr):
#     n = len(arr)
#     for i in range(n - 1):
#         for j in range(n - 1 - i):
#             if arr[j] > arr[j + 1]:
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]
#     return arr
###########################


# # STRETCH: implement the Count Sort function below
# def count_sort( arr, maximum=-1 ):

# 1. first create a list of length of the range of the numbers in the input array (smallest element = min, largest element = max of range)
# 2. initiallly this should be a list of zeros
# 3. iterate over your input array and for each element increase the amount in that place/index in the count array by one, for example if your input element has a value of 2, go to the index 2 in the count array count[2] and add 1 to zero, do this for all elements in input array
#4. for each element in count array add the previous element to the next
#5. create a new array the same length as input array
#6. iterate over input array and for each element do as follows:
# if input array element = 2, locate element in count array at index 2, suppose it is 4, insert the input array element(2) at the new array's index of count array element minus one (4 - 1 = 3), so at the new array index of 3

#     return arr