from queue_with_stacks import Queue

def test_Queue_exists():
    assert Queue

def test_instantion_queue():
    assert Queue()

def test_insert_one_queue():
    fruits = Queue()
    fruits.enqueue('Apples')
    expected = 'Apples'
    actual = fruits.front.value
    assert actual == expected


def test_insert_two_queue():
    fruits = Queue()
    fruits.enqueue('Apples')
    fruits.enqueue('Bananas')
    expected = 'Apples'
    actual = fruits.front.value
    assert actual == expected
    

def test_insert_three_stack():
    fruits = Queue()
    fruits.enqueue('Apples')
    fruits.enqueue('Bananas')
    fruits.enqueue('Pear')
    fruits.dequeue()
    expected = 'Pear'
    actual = fruits.top.value
    assert actual == expected
