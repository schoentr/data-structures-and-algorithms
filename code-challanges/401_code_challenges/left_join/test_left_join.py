from left_join.left_join import left_join
from hashtable.hashtable import Hashtable

def test_one():
    ht1 = Hashtable()
    ht1.add('chris', 'ball')
    ht1.add('tim', 'schoen')
    ht1.add('tony', 'tiger')
    ht1.add('uncle', 'joe')

    ht2 = Hashtable()
    ht2.add('chris','jones')
    ht2.add('jack','danials')
    ht2.add('tony','see')
    ht2.add('uncle','nickols')
    actual = left_join(ht1,ht2)
    assert actual ==  [['tim', 'schoen', None],['tony', 'tiger', 'see'],['uncle', 'joe', 'nickols'],['chris','ball','jones']]

def test_two():
    ht1 = Hashtable()
    ht1.add('chris', 'ball')
    ht1.add('tim', 'schoen')
    ht1.add('tony', 'tiger')
    ht1.add('evy', 'joe')

    ht2 = Hashtable()
    ht2.add('chris','jones')
    ht2.add('jack','danials')
    ht2.add('tony','see')
    ht2.add('uncle','nickols')
    actual = left_join(ht1,ht2)
    assert actual ==  [['tim', 'schoen', None],['evy', 'joe', None],['tony', 'tiger', 'see'],['chris','ball','jones']]

def test_three():
    ht1 = Hashtable()
    ht1.add('chris', 'ball')
    ht1.add('tim', 'schoen')
    ht1.add('tony', 'tiger')
    ht1.add('uncle', 'joe')

    ht2 = Hashtable()

    actual = left_join(ht1,ht2)
    assert actual ==  [['tim', 'schoen', None],['tony', 'tiger', None],['uncle', 'joe', None],['chris','ball', None]]
def test_four():
    ht1 = None
    ht2 = Hashtable()

    actual = left_join(ht1,ht2)
    assert actual ==  'No Hash Table Found'