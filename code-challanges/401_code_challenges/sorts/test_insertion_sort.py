from sorts.insertion_sort import insertion_sort
import numpy as np

     

     

def test_one():
    arr=[1,2,3,56,223,78,24,90,13]
    expected = [1,2,3,13,24,56,78,90,223]
    arr2=insertion_sort(arr)
    assert expected == arr2

def test_two():
    arr=['car','bar','tar','zar']
    expected = ['bar','car','tar','zar']
    insertion_sort(arr)
    assert expected == arr

def test_random():
    arr = [i for i in np.random.randint(1,101,100)]
    insertion_sort(arr)
    for j in range (1,len(arr)):
        assert arr[j-1]<= arr[j]

def test_empty_list():
    arr= []
    expected = []
    arr2=insertion_sort(arr)
    assert expected == arr


def test_reverse_list():
    arr= [5,4,3,2,1]
    expected = [1,2,3,4,5]
    arr2=insertion_sort(arr)
    assert expected == arr


def test_one_in_list():
    arr= [1]
    expected = [1]
    arr2=insertion_sort(arr)
    assert expected == arr


