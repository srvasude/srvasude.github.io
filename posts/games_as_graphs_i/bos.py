import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

plt.style.use('../../assets/modified-tufte.mplstyle')
np.random.seed(118887)

def create_bos_graph(node_color='#DC7027'):
    H = nx.Graph()
    H.add_nodes_from([
      (0, {"position": (0, 10)}),
      (1, {"position": (5, 10)}),
      (2, {"position": (8, 9)}),
      (3, {"position": (4, 8)}),
      (4, {"position": (7, 8.5)}),
      (5, {"position": (1, 6)}),
      (6, {"position": (7, 6)}),
      (7, {"position": (9, 5.5)}),
      (8, {"position": (4, 3)}),
      (9, {"position": (7, 2.5)}),
      (10, {"position": (0, 1)}),
      (11, {"position": (3, 0)}),
      (12, {"position": (6, 0)})])
    H.add_edges_from([
      (0, 1), (0, 3), (0, 5), (0, 10),
      (1, 2), (1, 4),
      (2, 4), (2, 7),
      (3, 4), (3, 5), (3, 8),
      (4, 6),
      (5, 10), (5, 11),
      (6, 7), (6, 8), (6, 9),
      (7, 9),
      (8, 11), (8, 12),
      (9, 12),
      (10, 11),
      (11, 12)])
    for v in H.nodes:
      H.nodes[v]['color'] = node_color
      H.nodes[v]['weight'] = 0
    return H
