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
        return self.last + 1
    

class Graph():
    '''
    Creates a graph using Networkx Library.
    '''
    graph = nx.Graph()
    IDAlloter = IDClass()

    def __init__(self):
        '''
        Constructor
        '''
        pass
    