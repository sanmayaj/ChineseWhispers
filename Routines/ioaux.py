'''
Created on Apr 5, 2013

@author: Sanmaya Jolly
'''

from graphmanip import create_weighted_edges_list
from clustermanip import create_clusters
from graph import Graph

def input_weighted_edges():
    print "Enter weighted edges as 3-tuples <Node1 Node2 Weight>"
    n = int(raw_input())
    li = []
    for i in range(n):
        li.append(tuple(raw_input().split()))
    return li

def input_nodes():
    print "Enter number of nodes"
    n = int(raw_input())
    li = []
    for i in range(n):
        li.append(raw_input())

def calc_weight(li1 = None, li2 = None):
    count = 0
    for item in li1:
        if li2.__contains__(item):
            count += 1
    return count

def file_input_test_data():
    test_data = file(r'C:\Users\Sanmaya Jolly\Documents\influential_bloggers_tags_data.txt')
    lineno = 0
    nodes = []
    for tagdata in test_data.readlines():
        tagdata = tagdata.rstrip()
        tags = tagdata.split(',')
        nodes.append(tuple([lineno, tags]))
        lineno += 1
    test_data.close()
    create_clusters(nodes)
    node_data = {}
    for i, tags in nodes:
        for j in range(i + 1, len(nodes)):
            weight = calc_weight(tags, nodes[j][1])
            if weight > 0:
                if node_data.__contains__(i):
                    node_data[i].append(tuple([j, weight]))
                else:
                    node_data[i] = [(j, weight)]
        i += 1
    graph_data = create_weighted_edges_list(node_data)
    #print graph_data
    g = Graph()
    for node in nodes:
        g.create_node(node[0], node[1])
    g.create_weighted_edges(graph_data)
    return g