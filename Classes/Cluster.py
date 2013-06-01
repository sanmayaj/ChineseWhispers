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
    cohesion = float()
    cohesion_count = int()
    node_tag_count = int()
    nodes_contained = int()
    tags_contained = list()

    def __init__(self, ID):
        '''
        Constructor
        '''
        self.node_list = []
        self.tags_contained = []
        self.label = ID
        self.nodes_contained = 0
        self.cohesion_count = 0
        self.node_tag_count = 0
        
    def add_node(self, name, tags):
        '''
        Adds a node to the cluster.
        '''
        self.node_list.append(name)
        self.nodes_contained += 1
        for tag in tags:
            if tag in self.tags_contained:
                self.cohesion_count += 1
            else:
                self.tags_contained.append(tag)
        self.node_tag_count += len(tags)
        self.cohesion = self.cohesion_count / self.node_tag_count
        
    def remove_node(self, g, ID):
        if not self.node_list.__contains__(ID):
            raise ValueError
        self.node_list.remove(ID)
        if not self.node_list:
            return self.label
        else:
            return None
        
    def strength(self):
        #return len(self.node_list)
        return self.cohesion
    
    def new_node_examination(self, new_node_tags):
        new_cohesion_count = self.cohesion_count
        for tag in new_node_tags:
            if tag in self.tags_contained:
                new_cohesion_count += 1
        new_node_tag_count = self.node_tag_count + len(new_node_tags)
        new_cohesion = new_cohesion_count/ new_node_tag_count
        if new_cohesion > self.cohesion:
            return True
        else:
            return False