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
    cohesion_count = float()
    node_tag_count = float()
    nodes_contained = int()
    tags_contained = dict()

    def __init__(self, ID):
        '''
        Constructor
        '''
        self.node_list = []
        self.tags_contained = {}
        self.label = ID
        self.nodes_contained = 0
        self.cohesion_count = 0
        self.node_tag_count = 0
        
    def is_empty(self):
        return self.nodes_contained == 0
        
    def add_node(self, name, tags):
        '''
        Adds a node to the cluster.
        '''
        self.node_list.append(name)
        if self.is_empty():
            for tag in tags:
                self.tags_contained[tag] = 1
            self.cohesion = 1
            self.nodes_contained = 1
            self.node_tag_count = len(tags)
            self.cohesion_count = self.node_tag_count
        else:
            self.nodes_contained += 1
            for tag in tags:
                if tag in self.tags_contained:
                    self.cohesion_count += 1
                    self.tags_contained[tag] += 1
                else:
                    self.tags_contained[tag] = 1
            self.node_tag_count += len(tags)
            self.cohesion = self.cohesion_count / self.node_tag_count
        
    def remove_node(self, g, ID):
        if not self.node_list.__contains__(ID):
            raise ValueError
        self.node_list.remove(ID)
        self.node_tag_count -= len(g.graf.node[ID]['tags'])
        self.nodes_contained -= 1
        for tag in g.graf.node[ID]['tags']:
            if self.tags_contained[tag] == 1:
                self.tags_contained.__delitem__(tag)
            else:
                self.tags_contained[tag] -= 1
                self.cohesion_count -= 1
        try:
            self.cohesion = self.cohesion_count/ self.node_tag_count
        except ZeroDivisionError:
            self.cohesion = 1
        if self.nodes_contained == 0:
            return self.label
        else:
            return None
        
    def strength(self):
        #return len(self.node_list)
        return self.cohesion
    
    def new_node_examination(self, new_node_tags):
        #print "New node being examined.. cluster has cohesion", self.cohesion
        new_cohesion_count = self.cohesion_count
        for tag in new_node_tags:
            if tag in self.tags_contained:
                new_cohesion_count += 1
        new_node_tag_count = self.node_tag_count + len(new_node_tags)
        #print "tag count changed from ", self.node_tag_count, "->", new_node_tag_count
        new_cohesion = new_cohesion_count/ new_node_tag_count
        #print "New cohesion calculated to be", new_cohesion
        if ((new_cohesion > self.cohesion) or (new_cohesion == self.cohesion and len(new_node_tags) > 0)):
            return True
        else:
            return False