def merge_sort(arr):
    """This function takes in a list and sorts the values in accending order.
    This sort is done in place  (modifing the existing list) with a merge sort.
    Arguments:
        list {list} -- [A list to be sorted (in place)]
    """
    if len(arr) >1:
        mid  = len(arr)//2
        l_arr = arr[:mid]
        r_arr = arr[mid:]
        merge_sort(l_arr)
        merge_sort(r_arr)
        i = j = k = 0  # i-- index of l_arr, j index of r_arr, k index of arr 
        while i < len(l_arr) and j <len(r_arr): 
            if l_arr[i] < r_arr[j]:  # check values to see order
                arr[k] = l_arr[i] 
                i+=1
            else: 
                arr[k] = r_arr[j] 
                j+=1
            k+=1
        while i < len(l_arr):  #append additional values if left in temp array
            arr[k] = l_arr[i] 
            i+=1
            k+=1
          
        while j < len(r_arr): 
            arr[k] = r_arr[j] 
            j+=1
            k+=1

   
