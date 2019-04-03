def partition(arr,start,end):
    """This fuction sorts the list around a pivot point, and returns the pivot point. Values less then the value at the pivot point, will be on the left side,   value higher will be on the right.  
    
    Arguments:
    Array, starting index,  ending index 
       
    Returns:
        [int] -- [index of the pivot point used for sorting]
    """

    i = start+1
    j= end
    pivot=arr[start]
    while (i<=j):
        while(arr[i]<pivot and i < end):
            i+=1
        while(arr[j]>pivot):
            j=j-1
        if (i<j):
            arr[i],arr[j]=arr[j],arr[i]
            i+=1
            j=j-1
        else:
            i=i+1
    arr[start]= arr[j]
    arr[j]=pivot
    return j

 
def quick_sort(arr,start=0,end=None):
    """This fucntion takes in a list and sorts the list using a quick sort algorthm.
    
    Arguments:
        arr {list}

    
    Keyword Arguments:
        start {int}  (default: {0})
        end {int} (default: {None})
    """

    if end==None:
        end=len(arr)-1
    if(start>=end):
        return
    pivot_loc = partition(arr,start, end)
    quick_sort(arr,start,pivot_loc-1)
    quick_sort(arr,pivot_loc+1,end)
