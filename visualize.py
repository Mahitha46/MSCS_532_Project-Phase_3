# visualize.py
import matplotlib.pyplot as plt
import networkx as nx
from graph import Graph
from matplotlib.cm import ScalarMappable
from matplotlib.colors import Normalize

def convert_to_nx(graph):
    G_nx = nx.DiGraph()
    for node in graph.nodes:
        G_nx.add_node(node)
    for u, neighbors in graph.edges.items():
        for v in neighbors:
            G_nx.add_edge(u, v)
    return G_nx

def draw_graph(graph, metric_dict=None, title="Social Network Graph", filename=None):
    G_nx = convert_to_nx(graph)
    pos = nx.spring_layout(G_nx, seed=42)
    fig, ax = plt.subplots(figsize=(8, 6))

    if metric_dict:
        values = [metric_dict.get(n, 0.0001) for n in G_nx.nodes()]
        norm = Normalize(vmin=min(values), vmax=max(values))
        sm = ScalarMappable(cmap=plt.cm.viridis, norm=norm)
        sm.set_array(values)
        nx.draw(
            G_nx, pos, with_labels=True, node_color=values,
            node_size=[1500 * max(0.1, v) for v in values],
            cmap=plt.cm.viridis, font_size=9, edge_color="gray", arrows=True, ax=ax
        )
        cbar = fig.colorbar(sm, ax=ax)
        cbar.set_label("Metric Value")
        ax.set_title(title)
    else:
        nx.draw(G_nx, pos, with_labels=True, node_color="lightblue",
                node_size=800, edge_color="gray", font_size=9, arrows=True, ax=ax)
        ax.set_title(title)

    ax.axis("off")
    fig.tight_layout()
    if filename:
        plt.savefig(filename, dpi=300)
    plt.show()
