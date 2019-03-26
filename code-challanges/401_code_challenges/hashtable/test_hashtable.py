from hashtable.hashtable import Hashtable


def test_exists():
    assert Hashtable
    

def test_instantion():
    """Can successfully instantiate an empty linked list
    """
    assert Hashtable()


def test_hash_one():
    test = Hashtable()
    actual = test.hash('tim')
    assert actual == 192


def test_add_one():
    test = Hashtable()
    actual = test.add('tim', 'texas')
    assert actual == ('tim', 'texas')


def test_get_one():
    test = Hashtable()
    test.add('chris', 'ball')
    test.add('tim', 'schoen')
    test.add('tony', 'tiger')
    test.add('uncle', 'joe')
    actual = test.get('tim')
    assert actual == ('schoen')


def test_get_two():
    test = Hashtable()
    test.add('chris', 'ball')
    test.add('tim', 'schoen')
    test.add('tony', 'tiger')
    test.add('uncle', 'joe')
    actual = test.get('uncle')
    assert actual == ('joe')


def test_get_three():
    test = Hashtable()
    test.add('chris', 'ball')
    test.add('tim', 'schoen')
    test.add('tony', 'tiger')
    test.add('uncle', 'joe')
    actual = test.get('foo')
    assert actual == None


def test_contains_one():
    test = Hashtable()
    test.add('chris', 'ball')
    test.add('tim', 'schoen')
    test.add('tony', 'tiger')
    test.add('uncle', 'joe')
    actual = test.contains('tim')
    assert actual == True


def test_contains_two():
    test = Hashtable()
    test.add('chris', 'ball')
    test.add('tim', 'schoen')
    test.add('tony', 'tiger')
    test.add('uncle', 'joe')
    actual = test.contains('uncle')
    assert actual == True


def test_contains_three():
    test = Hashtable()
    test.add('chris', 'ball')
    test.add('tim', 'schoen')
    test.add('tony', 'tiger')
    test.add('uncle', 'joe')
    actual = test.contains('foo')
    assert actual == False
