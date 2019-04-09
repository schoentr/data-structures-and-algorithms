from graphs.graph import Graph
from get_edge.get_edge import get_edges

def test_route_one_direct():
    g=Graph()
    pandora_v = g.add('pandora')
    arendelle_v = g.add('arendelle')
    metroville_v = g.add('metroville')
    monstropolus_v = g.add('monstropolus')
    naboo_v = g.add('naboo')
    narnia_v = g.add('narnia')
    g.add_edge(pandora_v,arendelle_v,150)
    g.add_edge(pandora_v,metroville_v,82)
    g.add_edge(arendelle_v,metroville_v,99)
    g.add_edge(arendelle_v,monstropolus_v,42)
    g.add_edge(naboo_v,monstropolus_v,73)
    g.add_edge(metroville_v,monstropolus_v,105)
    g.add_edge(naboo_v,metroville_v,26)
    g.add_edge(naboo_v,narnia_v,250)
    g.add_edge(narnia_v,metroville_v,37)
    actual = get_edges(g,['naboo','narnia'])
    expected= (True,250)
    assert actual == expected
def test_route_two_direct():
    g=Graph()
    pandora_v = g.add('pandora')
    arendelle_v = g.add('arendelle')
    metroville_v = g.add('metroville')
    monstropolus_v = g.add('monstropolus')
    naboo_v = g.add('naboo')
    narnia_v = g.add('narnia')
    g.add_edge(pandora_v,arendelle_v,150)
    g.add_edge(pandora_v,metroville_v,82)
    g.add_edge(arendelle_v,metroville_v,99)
    g.add_edge(arendelle_v,monstropolus_v,42)
    g.add_edge(naboo_v,monstropolus_v,73)
    g.add_edge(metroville_v,monstropolus_v,105)
    g.add_edge(naboo_v,metroville_v,26)
    g.add_edge(naboo_v,narnia_v,250)
    g.add_edge(narnia_v,metroville_v,37)
    actual = get_edges(g,['metroville','narnia'])
    expected= (True,37)
    assert actual == expected
def test_route_three_direct():
    g=Graph()
    pandora_v = g.add('pandora')
    arendelle_v = g.add('arendelle')
    metroville_v = g.add('metroville')
    monstropolus_v = g.add('monstropolus')
    naboo_v = g.add('naboo')
    narnia_v = g.add('narnia')
    g.add_edge(pandora_v,arendelle_v,150)
    g.add_edge(pandora_v,metroville_v,82)
    g.add_edge(arendelle_v,metroville_v,99)
    g.add_edge(arendelle_v,monstropolus_v,42)
    g.add_edge(naboo_v,monstropolus_v,73)
    g.add_edge(metroville_v,monstropolus_v,105)
    g.add_edge(naboo_v,metroville_v,26)
    g.add_edge(naboo_v,narnia_v,250)
    g.add_edge(narnia_v,metroville_v,37)
    actual = get_edges(g,['pandora','arendelle'])
    expected= (True,150)
    assert actual == expected
def test_route_four_direct():
    g=Graph()
    pandora_v = g.add('pandora')
    arendelle_v = g.add('arendelle')
    metroville_v = g.add('metroville')
    monstropolus_v = g.add('monstropolus')
    naboo_v = g.add('naboo')
    narnia_v = g.add('narnia')
    g.add_edge(pandora_v,arendelle_v,150)
    g.add_edge(pandora_v,metroville_v,82)
    g.add_edge(arendelle_v,metroville_v,99)
    g.add_edge(arendelle_v,monstropolus_v,42)
    g.add_edge(naboo_v,monstropolus_v,73)
    g.add_edge(metroville_v,monstropolus_v,105)
    g.add_edge(naboo_v,metroville_v,26)
    g.add_edge(naboo_v,narnia_v,250)
    g.add_edge(narnia_v,metroville_v,37)
    actual = get_edges(g,['naboo','metroville'])
    expected= (True,26)
    assert actual == expected
def test_route_one_one_stop():
    g=Graph()
    pandora_v = g.add('pandora')
    arendelle_v = g.add('arendelle')
    metroville_v = g.add('metroville')
    monstropolus_v = g.add('monstropolus')
    naboo_v = g.add('naboo')
    narnia_v = g.add('narnia')
    g.add_edge(pandora_v,arendelle_v,150)
    g.add_edge(pandora_v,metroville_v,82)
    g.add_edge(arendelle_v,metroville_v,99)
    g.add_edge(arendelle_v,monstropolus_v,42)
    g.add_edge(naboo_v,monstropolus_v,73)
    g.add_edge(metroville_v,monstropolus_v,105)
    g.add_edge(naboo_v,metroville_v,26)
    g.add_edge(naboo_v,narnia_v,250)
    g.add_edge(narnia_v,metroville_v,37)
    actual = get_edges(g,['naboo','metroville','arendelle'])
    expected= (True,125)
    assert actual == expected
def test_route_two_one_stop():
    g=Graph()
    pandora_v = g.add('pandora')
    arendelle_v = g.add('arendelle')
    metroville_v = g.add('metroville')
    monstropolus_v = g.add('monstropolus')
    naboo_v = g.add('naboo')
    narnia_v = g.add('narnia')
    g.add_edge(pandora_v,arendelle_v,150)
    g.add_edge(pandora_v,metroville_v,82)
    g.add_edge(arendelle_v,metroville_v,99)
    g.add_edge(arendelle_v,monstropolus_v,42)
    g.add_edge(naboo_v,monstropolus_v,73)
    g.add_edge(metroville_v,monstropolus_v,105)
    g.add_edge(naboo_v,metroville_v,26)
    g.add_edge(naboo_v,narnia_v,250)
    g.add_edge(narnia_v,metroville_v,37)
    actual = get_edges(g,['pandora','metroville','narnia'])
    expected= (True,119)
    assert actual == expected
def test_route_one_two_stop():
    g=Graph()
    pandora_v = g.add('pandora')
    arendelle_v = g.add('arendelle')
    metroville_v = g.add('metroville')
    monstropolus_v = g.add('monstropolus')
    naboo_v = g.add('naboo')
    narnia_v = g.add('narnia')
    g.add_edge(pandora_v,arendelle_v,150)
    g.add_edge(pandora_v,metroville_v,82)
    g.add_edge(arendelle_v,metroville_v,99)
    g.add_edge(arendelle_v,monstropolus_v,42)
    g.add_edge(naboo_v,monstropolus_v,73)
    g.add_edge(metroville_v,monstropolus_v,105)
    g.add_edge(naboo_v,metroville_v,26)
    g.add_edge(naboo_v,narnia_v,250)
    g.add_edge(narnia_v,metroville_v,37)
    actual = get_edges(g,['pandora','metroville','narnia','naboo'])
    expected= (True,369)
    assert actual == expected
def test_fail_one():
    g=Graph()
    pandora_v = g.add('pandora')
    arendelle_v = g.add('arendelle')
    metroville_v = g.add('metroville')
    monstropolus_v = g.add('monstropolus')
    naboo_v = g.add('naboo')
    narnia_v = g.add('narnia')
    g.add_edge(pandora_v,arendelle_v,150)
    g.add_edge(pandora_v,metroville_v,82)
    g.add_edge(arendelle_v,metroville_v,99)
    g.add_edge(arendelle_v,monstropolus_v,42)
    g.add_edge(naboo_v,monstropolus_v,73)
    g.add_edge(metroville_v,monstropolus_v,105)
    g.add_edge(naboo_v,metroville_v,26)
    g.add_edge(naboo_v,narnia_v,250)
    g.add_edge(narnia_v,metroville_v,37)
    actual = get_edges(g,['pandora','naboo','narnia','naboo'])
    expected= (False,0)
    assert actual == expected
