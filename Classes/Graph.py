'''
Created on Mar 28, 2013

@author: Sanmaya Jolly
'''
import networkx as nx
        
class IDClass():
    '''
    Allots ID's to every node.
    This functions like Django's AutoField. 
    '''
    last = int()
    
    def __init__(self):
        self.last = 0
    
    def allot_id(self):
        self.last += 1
        return self.last
    

class Graph():
    '''
    Creates a graph using Networkx Library.
    '''
    graph = nx.Graph()
    IDAllotter = IDClass()

    def __init__(self):
        '''
        Constructor
        '''
        self.graph = nx.Graph()
        self.graph.clear()
        self.IDAllotter = IDClass()
    
    def create_node(self, node_data):
        self.graph.add_node(node_data, { 'label' : self.IDAllotter.allot_id() })
        
    def create_edge(self, node1, node2, weight = None):
        if weight:
            self.graph.add_weighted_edges_from( [ (node1, node2, weight) ] )
        else:
            self.graph.add_weighted_edges_from( [ (node1, node2, 1) ] )

    def create_weighted_edges(self, weighted_edge_list):
        self.graph.add_weighted_edges_from(weighted_edge_list)
        
    def return_neighbours(self, node):
        for n, nbrs in self.graph.adjacency_iter():
            if n == node:
                return nbrs
    