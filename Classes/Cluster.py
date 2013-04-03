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
    label = int()

    def __init__(self, ID):
        '''
        Constructor
        '''
        self.node_list = []
        self.label = ID
        
    def add_node(self, ID):
        '''
        Adds a node's ID to the list of a cluster.
        '''
        self.node_list.append(ID)
        
    def remove_node(self, g, ID):
        if not self.node_list.__contains__(ID):
            raise ValueError
        self.node_list.remove(ID)
        if not self.node_list:
            return self.label
        else:
            return None