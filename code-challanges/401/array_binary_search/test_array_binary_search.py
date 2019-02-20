from array_binary_search import binary_search

def test_list_length_four_no():
    actual = binary_search([1,2,3,4],6)
    expected = -1
    assert expected == actual
def test_list_length_four_yes():
    actual = binary_search([1,2,3,4],4)
    expected = 3
    assert expected == actual
def test_list_length_nine_no():
    actual = binary_search([1,2,3,4,5,0,7,8,9],6)
    expected = -1
    assert expected == actual
def test_list_length_nine_yes():
    actual = binary_search([1,2,3,4,5,6,7,8,9],6)
    expected = 5
    assert expected == actual