from stacks_and_queues import Stack, Queue

def test_stack_exists():
    assert Stack

def test_instantion_stack():
    assert Stack()

def test_insert_one_stack():
    fruits = Stack()
    fruits.push('Apples')
    expected = 'Apples'
    actual = fruits.
    assert actual == expected


def test_insert_two_stack():
    fruits = Stack()
    fruits.push('Apples')
    fruits.push('Bananas')
    expected = 'Bananas'
    actual = fruits.top.value
    assert actual == expected
    

def test_insert_three_stack():
    fruits = Stack()
    fruits.push('Apples')
    fruits.push('Bananas')
    fruits.push('Pear')
    expected = 'Pear'
    actual = fruits.top.value
    assert actual == expected


def test_dequeue_until_empty_stack():
    fruits = Stack()
    fruits.push('Apples')
    fruits.push('Bananas')
    fruits.push('Pear')
    while fruits.top:
        fruits.pop()
    expected = None
    actual = fruits.top
    assert actual == expected

def test_peek():
    fruits = Stack()
    fruits.push('Apples')
    fruits.push('Bananas')
    fruits.push('Pear')
    expected = 'Pear'
    actual = fruits.peek()
    assert actual == expected


def test_queue_exists():
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
    expected = 'Bananas'
    actual = fruits.rear.value
    expected = 'Apples'
    actual = fruits.front.value
    assert actual == expected
    

def test_insert_three_queue():
    fruits = Queue()
    fruits.enqueue('Apples')
    fruits.enqueue('Bananas')
    fruits.enqueue('Pear')
    expected = 'Pear'
    actual = fruits.rear.value
    expected = 'Apples'
    actual = fruits.front.value
    assert actual == expected

def test_dequere_one():
    fruits = Queue()
    fruits.enqueue('Apples')
    fruits.enqueue('Bananas')
    fruits.enqueue('Pear')
    fruits.dequeue()
    expected = 'Bananas'
    actual = fruits.front.value
    assert actual == expected




def test_dequeue_until_empty_queue():
    fruits = Queue()
    fruits.enqueue('Apples')
    fruits.enqueue('Bananas')
    fruits.enqueue('Pear')
    while fruits.front:
        fruits.dequeue()
    expected = None
    actual = fruits.front
    assert actual == expected

def test_peek_queue():
    fruits = Queue()
    fruits.enqueue('Apples')
    fruits.enqueue('Bananas')
    fruits.enqueue('Pear')
    expected = 'Apples'
    actual = fruits.peek()
    assert actual == expected
    
