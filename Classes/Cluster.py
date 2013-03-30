'''
Created on Mar 30, 2013

@author: Sanmaya Jolly
'''

import networkx as nx
from classes.graph import Graph

class Cluster():
    '''
    Defines a cluster. A cluster consists of networkx nodes' id's.
    '''
    node_list = list()

    def __init__(self):
        '''
        Constructor
        '''
        node_list = []
        
    def add_node_to_cluster(self, ID):
        '''
        Adds a node's ID to the list of a cluster.
        '''
        self.node_list.append(ID)