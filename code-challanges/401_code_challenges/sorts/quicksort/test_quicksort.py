from sorts.quicksort.quicksort import quick_sort
import numpy as np

def test_one():
    arr=[1,2,3,56,223,78,24,90,13]
    expected = [1,2,3,13,24,56,78,90,223]
    quick_sort(arr)
    assert expected == arr

def test_two():
    arr=['car','bar','tar','zar']
    expected = ['bar','car','tar','zar']
    quick_sort(arr)
    assert expected == arr

def test_random():
    arr = [i for i in np.random.randint(1,101,100)]
    quick_sort(arr)
    for j in range (1,len(arr)):
        assert arr[j-1]<= arr[j]

def test_empty_list():
    arr= []
    expected = []
    quick_sort(arr)
    assert expected == arr
