from .repeat_word import repeat_word
from hashtable.hashtable import Hashtable

def test_one():
    string="mouse dog cat dog"
    actual=repeat_word(string)
    # print (actual)
    assert 'dog' == actual
def test_three():
    string="mouse Dog cat dog"
    actual=repeat_word(string)
    # print (actual)
    assert 'dog' == actual
def test_four():
    string="mouse tim cat dog Tim Schoen"
    actual=repeat_word(string)
    # print (actual)
    assert 'tim' == actual
def test_five():
    string="mouse dog cat dog cheese cheese"
    actual=repeat_word(string)
    # print (actual)
    assert 'dog' == actual
def test_six():
    string="mouse dog cat cow bat stuff"
    actual=repeat_word(string)
    # print (actual)
    assert 'No matching Words' == actual