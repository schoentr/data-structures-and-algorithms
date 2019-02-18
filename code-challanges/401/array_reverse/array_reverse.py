def list_reverse(list1):
    new_list = []
    for i in range(len(list1)-1, -1, -1):
        new_list.append(list1[i])
    return new_list

test = [1, 2, 3, 4, 5, 6]
print(test)
print(list_reverse(test))
