'''
Created on Apr 5, 2013

@author: Sanmaya Jolly
'''

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