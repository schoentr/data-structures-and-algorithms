
def insertion_sort(input_list):
    """This function takes in a list and sorts the values in accending order.
    This sort is done in place  (modifing the existing list)


    Arguments:
        list {list} -- [A list to be sorted (in place)]
    """
    for index in range(1, len(input_list)):
        value = input_list[index]
        i = index - 1
        while i >= 0:
            if value < input_list[i]:
                input_list[i+1] = input_list[i]
                input_list[i] = value
                i = i - 1
            else:
                break
    return input_list

