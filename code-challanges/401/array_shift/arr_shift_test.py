from arr_shift import insertShiftArray

def test_array_four_elements():
    actual = insertShiftArray([1,2,3,4],6)
    expected = [1,2,6,3,4]
    assert expected == actual
def test_array_six_elements():
    actual = insertShiftArray([1,2,3,4,9,10],6)
    expected = [1,2,3,6,4,9,10]
    assert expected == actual
def test_array_2_elements():
    actual = insertShiftArray([1,2],6)
    expected = [1,6,2]
    assert expected == actual