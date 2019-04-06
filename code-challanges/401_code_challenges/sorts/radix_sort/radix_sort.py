def radix_sort(alist, base=10):
    if alist == []:
        return
 
    def key_factory(digit, base):
        def key(alist, index):
            return ((alist[index]//(base**digit)) % base)
        return key
    largest = max(alist)
    exp = 0
    while base**exp <= largest:
        alist = counting_sort(alist, base - 1, key_factory(exp, base))
        exp = exp + 1
    return alist
 

def counting_sort(arr, exp1): 
  
    n = len(arr) 
  
    # The output array elements that will have sorted arr 
    output = [0] * (n) 
  
    # initialize count array as 0 
    count = [0] * (10) 
  
    # Store count of occurrences in count[] 
    for i in range(0, n): 
        index = (arr[i]/exp1) 
        count[ (index)%10 ] += 1
  
    # Change count[i] so that count[i] now contains actual 
    #  position of this digit in output array 
    for i in range(1,10): 
        count[i] += count[i-1] 
  
    # Build the output array 
    i = n-1
    while i>=0: 
        index = (arr[i]/exp1) 
        output[ count[ (index)%10 ] - 1] = arr[i] 
        count[ (index)%10 ] -= 1
        i -= 1
  
    # Copying the output array to arr[], 
    # so that arr now contains sorted numbers 
    i = 0
    for i in range(0,len(arr)): 
        arr[i] = output[i]
# def counting_sort(alist, largest, key):
#     c = [0]*(largest + 1)
#     for i in range(len(alist)):
#         c[key(alist, i)] = c[key(alist, i)] + 1
 
#     # Find the last index for each element
#     c[0] = c[0] - 1 # to decrement each element for zero-based indexing
#     for i in range(1, largest + 1):
#         c[i] = c[i] + c[i - 1]
 
#     result = [None]*len(alist)
#     for i in range(len(alist) - 1, -1, -1):
#         result[c[key(alist, i)]] = alist[i]
#         c[key(alist, i)] = c[key(alist, i)] - 1
 
#     return result
    