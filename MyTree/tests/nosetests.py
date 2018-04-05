from MyTree import MyTree

t = None


def test_010_create():
    global t
    print("test_010_create")
    t = MyTree()
    assert t


def test__030_add_nodes():
    global t
    print("test__030_add_nodes")
    for i in range(10):
        t.add_node(str(i))


def test_040_count_nodes():
    global t
    print("test__040_count_nodes")
    assert t.count_nodes() == 10


def test_050_find_node_true():
    global t
    print("test__050_find_node_true")
    status, *node = t.find_node('2')
    assert status == True


def test_050_find_node_false():
    global t
    print("test_050_find_node_false")
    status, *node = t.find_node('22')
    assert status == False


def test_060_add_edge_with_attrs_true():
    global t
    print("test_060_add_edge_true")
    assert t.add_edge(t.find_node('1'), t.find_node('2'), {"name": "edge_1"}) == True


def test_060_add_edge_no_attrs_true():
    global t
    print("test_060_add_edge_no_attrs_true")
    assert t.add_edge(t.find_node('3'), t.find_node('4')) == True


#def test_070_count_edges():
#    global t
#    print("test_070_count_edges")
#    assert t.count_edges() == 2

def test_080_load_file():
    global t
    print("test_080_load_file")
    nodes,jobs = t.load_file("test_flow.txt")
    assert len(nodes)==21  and len(jobs)==19

def test_90_load_file_and_class():
    global t
    print("test_90_load_file_and_class")
    t=MyTree()
    nodes, jobs = t.load_file("test_flow.txt")
    for j in jobs:
        t.add_edge(j[0],j[1])
    assert t.count_edges()==19


def test_100_test_draw():
    global t
    #import matplotlib.pyplot as plt
    #plt.draw(t.net)
    assert True