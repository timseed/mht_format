import networkx as nx


class MyTree(object):

    def __init__(self):
        junk = 1
        self.net = nx.Graph()

    def count_nodes(self):
        return len(self.net.nodes)

    def add_node(self, node_name):
        self.net.add_node(node_name)
        return True

    def find_node(self, node_name):
        if node_name in self.net.nodes:
            return True, (1)
        else:
            return False, ()

    def add_edge(self, from_node, to_node, my_attrs=None):
        try:
            edge=self.net.add_edge(from_node, to_node)
            if my_attrs is not None:
                self.net[from_node][to_node].update(my_attrs)
            return True
        except Exception as err:
            return False

    def count_edges(self):
        ee=[e for e in self.net.edges]
        a=len(ee)
        return a

    def load_file(self,filename,add_start=False):
        """
        Read a Comma delimited file like

            #Comment
            job1,job2,job3
            job4,job3,job5

        :param filename:
        :param add_start: Do we add a "Start_node" before the flows ?
        :return: list of a string of Job names , list or tuples of job-pairs
        """
        nodes=[]
        flows=[]
        with open(filename,"rt") as infile:
            for line in infile:
                if not line.startswith("#"):
                    line=line.strip()
                    jobs=line.split(',')


                    if add_start:
                        nodes.append("Start")

                    for n in jobs:
                        nodes.append(n)

                    for n in range(len(jobs) - 1):
                        flows.append((jobs[n],jobs[n+1]))

                    if add_start:
                        flows.append(("Start",jobs[0]))

        junk=1
        return sorted(list(set(nodes))),set(flows)

