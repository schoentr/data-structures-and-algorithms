from queue_with_stacks.queue_with_stacks import Queue

def test_Queue_exists():
    assert Queue

def test_instantion_queue():
    assert Queue()

def test_insert_one_queue():
    fruits = Queue()
    fruits.enqueue('Apples')
    expected = 'Apples'
    actual = fruits.input_stack.peek()
    assert actual == expected


def test_insert_two_queue():
    fruits = Queue()
    fruits.enqueue('Apples')
    fruits.enqueue('Bananas')
    expected = 'Bananas'
    actual = fruits.input_stack.peek()
    assert actual == expected
    

def test_insert_three_stack():
    fruits = Queue()
    fruits.enqueue('Apples')
    fruits.enqueue('Bananas')
    fruits.enqueue('Pear')
    fruits.dequeue()
    expected = 'Pear'
    actual = fruits.input_stack.peek()
    assert actual == expected

def test_insert_three_stack():
    fruits = Queue()
    fruits.enqueue('Apples')
    fruits.enqueue('Bananas')
    fruits.enqueue('Pear')
    fruits.dequeue()
    expected = 'Bananas'
    actual = fruits.output.peek()
    assert actual == expected
