'''
Created on Apr 3, 2013

@author: Sanmaya Jolly
'''

#from graph import Graph
#import networkx as nx

def get_max_weighted_edges(graph, node_name):
    maxw = 0
    maxl = []
    for n, nbrs in graph.adjacency_iter():
        if n == node_name:
            for nbr, eattr in nbrs.items():
                weight = eattr['weight']
                if weight > maxw:
                    maxw = weight
                    maxl = [(nbr, graph.node[nbr]['label'])]
                elif weight == maxw:
                    maxl.append((nbr, graph.node[nbr]['label']))
    return (maxw, maxl)


def change_node_label(graph, node_name, new_label):
    old_label = graph.node[node_name]['label']
    graph.node[node_name]['label'] = new_label
    return old_label