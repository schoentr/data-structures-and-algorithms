from linked_list.linked_listf import LinkedList

def ll_merge(list_A, list_B):
    curr_B = list_B.head
    curr_A = list_A.head
    temp_C = None
    while curr_A._next and curr_B:
        curr_B = list_B.head
        temp_A = curr_A._next
        temp_B = curr_B._next
        # if curr_B._next._next:
        #     temp_C = curr_B._next._next
        curr_A._next = curr_B
        curr_B._next = temp_A
        list_B.head = temp_B
        curr_A= curr_A._next._next
        curr_B=list_B.head  
    if curr_B:
        curr_A._next=curr_B
    return list_A.head

ones = LinkedList()
ones.insert('1')
ones.insert('2')
ones.insert('3')
ones.insert('4')
ones.insert('5')

print(ones.print())
tens = LinkedList()
tens.insert('10')
tens.insert('20')
# tens.insert('30')
# tens.insert('40')
# tens.insert('50')
print(tens.print())

ll_merged(ones,tens)
print(ones.print())
