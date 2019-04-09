from graphs.graph import Graph

def test_neighbors():
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
    g.add_edge(vertex_a, vertex_c)
    g.add_edge(vertex_a, vertex_d)
    g.add_edge(vertex_e, vertex_c)
    g.add_edge(vertex_e, vertex_d)
    g.add_edge(vertex_e, vertex_f)
    g.add_edge(vertex_f, vertex_g)
    g.add_edge(vertex_h, vertex_g)
    g.add_edge(vertex_b, vertex_g)
 
    actual = g.breadth_first('a')
    assert actual == []