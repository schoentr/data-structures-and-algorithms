from stacks_and_queues.stacks_and_queues import Queue
from multi_bracket_validation.multi_bracket_validation import bracket_validation


def test_one():
    assert bracket_validation('th{his(hlie}v[') == False


def test_two():
    assert bracket_validation('{}') == True


def test_three():
    assert bracket_validation('()') == True


def test_four():
    assert bracket_validation('(') == False


def test_five():
    assert bracket_validation(')') == False


def test_six():
    assert bracket_validation('[]') == True


def test_seve():
    assert bracket_validation('[') == False


def test_eight():
    assert bracket_validation(']') == False


def test_nine():
    assert bracket_validation('([dog]{cat})') == True


def test_ten():
    assert bracket_validation('This(should} not ) pass') == False


def test_eleven():
    assert bracket_validation('[this(sdf{sdf(sdfsdf)})]') == True


def test_twelve():
    assert bracket_validation('{sdfsdf ()sdfsdf') == False


def test_thirteen():
    assert bracket_validation('') == True
