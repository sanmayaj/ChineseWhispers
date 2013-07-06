'''
Created on Apr 3, 2013

@author: Sanmaya Jolly
'''

import random
import clusterglobals
from cluster import Cluster

def random_cluster(li):
    length = len(li)
    if length > 1:
        x = random.randint(0, length - 1)
        return li[x]
    elif length == 1:
        return li[0]
    if li == []:
        return None
    
def  probabilistic_best_cluster(node_data, li):
    #print "Max weighted cluster list is: ", {clust.label for clust in li}, "node data", node_data
    if li == []:
        return None
    elif li.__len__() == 1:
        return li[0] if li[0].new_node_examination(node_data) else None
    best_p_fact = 0.0
    for cluster in li:
        common = 0
        for tag in node_data:
            if tag in cluster.tags_contained:
                common += 1
        #print "cluster", cluster.label, "has", common, "common tags"
        p_fact = common / len(node_data)
        best_fit_cluster = None
        if best_p_fact <= p_fact:
            best_p_fact = p_fact
            best_fit_cluster = cluster
        elif best_p_fact == p_fact and cluster.new_node_examination(node_data):
            best_fit_cluster = cluster
    return best_fit_cluster

def create_clusters(node_data):
    for node_name, node_tags in node_data:
        c =  Cluster(ID = int(node_name))
        c.add_node(node_name, node_tags)
        clusterglobals.clusters_list.append(c)
