""" Arrary Binary Seach Mod  """


def binary_search(arr, value):
    """ Binary Search takes array and value to search """
    """ returns index or-1"""
    count = len(arr)
    midpoint = count // 2
    start_index = 0
    end_index = count - 1
    while value != arr[start_index+midpoint] and count > 1:
        # import pdb; pdb.set_trace()
        if value > arr[midpoint+start_index]:
            start_index = midpoint
            count = count - (midpoint)
            midpoint = count // 2
        else:
            end_index = end_index - midpoint
            count = count - midpoint
            midpoint = count // 2
        
    if value == arr[midpoint+start_index]:
        return midpoint + start_index
    else:
        return -1
        
# print(binary_search([1, 2, 3, 4, 5, 6], 9))

    