from graphs.graph import Graph

def test_neighbors_one():
    g = Graph()
    vertex_a = g.add('a')
    vertex_b = g.add('b')
    vertex_c = g.add('c')
    vertex_d = g.add('d')
    vertex_e = g.add('e')
    vertex_f = g.add('f')
    vertex_g = g.add('g')
    vertex_h = g.add('h')

    g.add_edge(vertex_a, vertex_b)
    g.add_edge(vertex_c, vertex_g)
    g.add_edge(vertex_b, vertex_c)
    g.add_edge(vertex_b, vertex_d)
    g.add_edge(vertex_e, vertex_d)
    g.add_edge(vertex_d, vertex_h)
    g.add_edge(vertex_f, vertex_h)
    g.add_edge(vertex_d, vertex_f)
    g.add_edge(vertex_d, vertex_a)
 
    actual = g.depth_first('a')
    
    assert actual == ['a', 'b', 'c', 'g', 'd', 'e', 'h', 'f']
def test_neighbors_two():
    g = Graph()
    vertex_a = g.add('a')
    vertex_b = g.add('b')
    vertex_c = g.add('c')
    vertex_d = g.add('d')
    vertex_e = g.add('e')
    vertex_f = g.add('f')
    vertex_g = g.add('g')
    vertex_h = g.add('h')

    g.add_edge(vertex_a, vertex_b)
    g.add_edge(vertex_c, vertex_g)
    g.add_edge(vertex_b, vertex_c)
    g.add_edge(vertex_b, vertex_d)
    g.add_edge(vertex_e, vertex_d)
    g.add_edge(vertex_d, vertex_h)
    g.add_edge(vertex_f, vertex_h)
    g.add_edge(vertex_d, vertex_f)
    g.add_edge(vertex_d, vertex_a)
 
    actual = g.depth_first('d')
    
    assert actual == ['d', 'b', 'a', 'c', 'g', 'e', 'h', 'f']

def test_neighbors_three():
    g = Graph()
    vertex_a = g.add('a')
    vertex_b = g.add('b')
    vertex_c = g.add('c')
    vertex_d = g.add('d')
    vertex_e = g.add('e')
    vertex_f = g.add('f')
    vertex_g = g.add('g')
    vertex_h = g.add('h')

    g.add_edge(vertex_a, vertex_b)
    g.add_edge(vertex_c, vertex_g)
    g.add_edge(vertex_b, vertex_c)
    g.add_edge(vertex_b, vertex_d)
    g.add_edge(vertex_e, vertex_d)
    g.add_edge(vertex_d, vertex_h)
    g.add_edge(vertex_f, vertex_h)
    g.add_edge(vertex_d, vertex_f)
    g.add_edge(vertex_d, vertex_a)
 
    actual = g.depth_first('f')
    
    assert actual == ['f', 'h', 'd', 'b', 'a', 'c', 'g', 'e']