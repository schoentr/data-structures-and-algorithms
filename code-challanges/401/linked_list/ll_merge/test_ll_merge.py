# from linked_list.linked_list import LinkedList
# from linked_list.ll_merge.ll_merge import ll_merge

# def test_even_list():
#    ones = LinkedList()
#    ones.insert('1')
#    ones.insert('2')
#    ones.insert('3')
#    ones.insert('4')
#    ones.insert('5')
#    tens = LinkedList()
#    tens.insert('10')
#    tens.insert('20')
#    tens.insert('30')
#    tens.insert('40')
#    tens.insert('50')
#    expected ='1, 10, 2, 20, 3, 30, 4, 40, 5, 50, '
#    ll_merge(ones,tens)
#    actual = ones.print()
#    assert ones.head.value == '1'
#    assert expected == actual

# def test_short_list_A():
#    ones = LinkedList()
#    ones.insert('1')
#    ones.insert('2')
#    ones.insert('3')
#    tens = LinkedList()
#    tens.insert('10')
#    tens.insert('20')
#    tens.insert('30')
#    tens.insert('40')
#    tens.insert('50')
#    expected ='1, 10, 2, 20, 3, 30, 40, 50, '
#    ll_merge(ones,tens)
#    actual = ones.print()
#    assert ones.head.value == '1'
#    assert expected == actual

# def test_short_list_B():
#    ones = LinkedList()
#    ones.insert('1')
#    ones.insert('2')
#    ones.insert('3')
#    ones.insert('4')
#    ones.insert('5')
#    tens = LinkedList()
#    tens.insert('10')
#    tens.insert('20')
#    tens.insert('30')
#    expected ='1, 10, 2, 20, 3, 30, 4, 5, '
#    ll_merge(ones,tens)
#    actual = ones.print()
#    assert ones.head.value == '1'
#    assert expected == actual
