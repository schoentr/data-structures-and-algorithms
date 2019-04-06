from graphs.graph import Graph


def test_class():
    assert Graph


def test_instance():
    assert Graph()


def test_add_vertex():
    g = Graph()
    vertex = g.add('apple')
    assert 'apple' in g._graph
    assert vertex
    assert g._graph['apple'] == []


def test_edge():
    g = Graph()
    vertex_apple = g.add('apple')
    vertex_banana = g.add('banana')
    g.add_edge(vertex_apple, vertex_banana, 3)
    assert g._graph['apple'] == [('banana', 3)]
    assert g._graph['banana'] == [('apple', 3)]


def test_edge_two():
    g = Graph()
    vertex_apple = g.add('apple')
    vertex_banana = g.add('banana')
    vertex_cake = g.add('cake')
    vertex_dog = g.add('dog')
    vertex_egg = g.add('egg')
    g.add_edge(vertex_apple, vertex_banana)
    g.add_edge(vertex_cake, vertex_dog, 2)
    g.add_edge(vertex_dog, vertex_egg, 4)
    assert g._graph['apple'] == [('banana', 1)]
    assert g._graph['banana'] == [('apple', 1)]
    assert g._graph['dog'] == [('cake', 2), ('egg', 4)]


def test_get_vertices():
    g = Graph()
    vertex_apple = g.add('apple')
    vertex_banana = g.add('banana')
    vertex_cake = g.add('cake')
    expected = g.get_vertices()
    assert expected == ['apple', 'banana', 'cake']


def test_size():
    g = Graph()
    vertex_apple = g.add('apple')
    vertex_banana = g.add('banana')
    vertex_cake = g.add('cake')
    expected = g.size()
    assert expected == 3
    vertex_banana = g.add('dog')
    vertex_cake = g.add('egg')
    expected = g.size()
    assert expected == 5


def test_neighbors():
    g = Graph()
    vertex_apple = g.add('apple')
    vertex_banana = g.add('banana')
    vertex_cake = g.add('cake')
    vertex_dog = g.add('dog')
    vertex_egg = g.add('egg')
    vertex_foo = g.add('foo')
    g.add_edge(vertex_apple, vertex_banana)
    g.add_edge(vertex_cake, vertex_dog, 2)
    g.add_edge(vertex_dog, vertex_egg, 4)
    expected_apple = g.get_neighbors(vertex_apple)
    expected_dog = g.get_neighbors(vertex_dog)
    expected_foo = g.get_neighbors(vertex_foo)
    assert expected_apple == [('banana', 1)]
    assert expected_dog == [('cake', 2), ('egg', 4)]
    assert expected_foo == []
