'''
Created on Mar 30, 2013

@author: Sanmaya Jolly
'''

import networkx as nx

class Cluster():
    '''
    Defines a cluster. A cluster consists of networkx nodes' id's.
    '''
    node_list = list()

    def __init__(self):
        '''
        Constructor
        '''
        self.node_list = []
        
    def add_node(self, ID):
        '''
        Adds a node's ID to the list of a cluster.
        '''
        self.node_list.append(ID)
        
    def remove_node(self, ID):
        if not self.node_list.__contains__(ID):
            raise ValueError
        self.node_list.remove(ID)