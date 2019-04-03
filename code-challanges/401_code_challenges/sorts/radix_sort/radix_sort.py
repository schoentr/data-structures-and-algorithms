def radix_sort(inpt_list, base=10):
    """This sort takes in  a list of positive  numbers and returns the list sorted in place.
    
    Arguments:
        inpt_list {[list]} -- [Unsorted List]
    
    Keyword Arguments:
        base {int} -- [description] (default: {10})
    
    Returns:
        [list] -- [Sorted List]
    """

    if inpt_list == []:
        return
 
    def key_factory(digit, base):
        """This fuction creates the keys.  
        
        Arguments:
            digit {[type]} -- [description]
            base {[type]} -- [description]
        
        Returns:
            [type] -- [description]
        """

        def key(alist, index):
            """This helper function takes in the unsorted list and and index and returns the digit at that location.
            
            Arguments:
                alist {list} -- [unsorted list]
                index {int} -- [index of list to be evaluated]
            
            Returns:
                [int] -- [the digit that is in the place being evaluated]
            """

            return ((inpt_list[index]//(base**digit)) % base)
        return key
    largest = max(inpt_list)
    exp = 0
    while base**exp <= largest: #checks to see if all values have been covered
        inpt_list = count_sort(inpt_list, key_factory(exp, base),base-1)
        exp = exp + 1
    return alist

def count_sort(inpt_list,key,list_range):
    """ This sorts a list by counting the number of occurances a given digt occurs, 
    Arguments:
        inpt_list {list} 
        key {int}
        list_range {int} 
    
    Returns:
        [list] 
    """

    count_list= [0]*(list_range + 1)
    for i in range(len(inpt_list)):
        count_list[key(inpt_list, i)] = count_list[key(inpt_list, i)] + 1
    count_list[0] = count_list[0] - 1 
    for i in range(1, list_range + 1):
        count_list[i] = count_list[i] + count_list[i - 1]
    result = [None]*len(inpt_list)
    for i in range(len(inpt_list) - 1, -1, -1):
        result[count_list[key(inpt_list, i)]] = inpt_list[i]
        count_list[key(inpt_list, i)] = count_list[key(inpt_list, i)] - 1
 
    return result