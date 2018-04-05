# My Tree

This is a project that will hopefully allow me to generate a Custom Network (not Tree).

The purpose of the Network/Tree is to feed a d3 process which will allow for dynamic Work-flow visualisation

#Requirements

  - networkx
  
  
  
  
#IPython Visualisation

To see the state of the network before you involve D3 looks at this code


```python
import MyTree
import networkx as nx
import matplotlib.pyplot as plt

mt=MyTree.MyTree()

jobs,job_pairs=mt.load_file("test_flow.txt",add_start=True)

for jp in job_pairs:
    mt.add_edge(jp[0],jp[1])

nx.draw_networkx(mt.net)
```


Please note: add_start=True.

The chart looks like this

