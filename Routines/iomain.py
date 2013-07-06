'''
Created on Apr 3, 2013

@author: Sanmaya Jolly
'''

from graph import Graph
from cluster import Cluster
from graphmanip import *
from clustermanip import random_cluster, probabilistic_best_cluster
from ioaux import file_input_test_data as input_from_file
import clusterglobals

def p_factored_clustering(g):
    for node_name, node_data in g.graf.nodes(data = True):
        max_weight_clusters_list  = get_max_weighted_clusters(g, node_name)
        new_cluster = probabilistic_best_cluster(node_data['tags'], max_weight_clusters_list)
        '''try:
            old_cluster_label = change_node_cluster(g, node_name, new_cluster.label)
            old_cluster = clusterglobals.get_cluster(old_cluster_label)
            old_cluster.remove_node(g, node_name)
            new_cluster.add_node(node_name, node_data['tags'])
            clusterglobals.replace_cluster(new_cluster)
            clusterglobals.replace_cluster(old_cluster)
            print node_name, "of cluster", old_cluster_label, "has been moved to", new_cluster.label
        except AttributeError:
            print node_name, "of cluster", node_data['CLID'], "stays"
            pass'''
        if new_cluster:
            old_cluster_id = g.graf.node[node_name]['CLID']
            tags = g.graf.node[node_name]['tags']
            old_cluster = get_cluster(old_cluster_id)
            st = old_cluster.remove_node(g, node_name)
            if st == None:
                replace_cluster(old_cluster)
            else:
                replace_cluster(old_cluster, remove = True)
            new_cluster.add_node(node_name, tags)
            replace_cluster(new_cluster)
            change_node_cluster(g, node_name, new_cluster.label)
        else:
            pass
        clusterglobals.print_clusters()

if __name__ == '__main__':
    g = Graph()
    g = input_from_file()
    mode = 0
    print "1. Random\n2. Probabilistic"
    mode = int(raw_input())
    if mode == 1:
        random_classification(g)
    else:
        p_factored_clustering(g)
        #calculated_clustering(g)
    for c in clusterglobals.clusters_list:
        print c.label, c.node_list, c.tags_contained , c.nodes_contained
        

