'''
Created on Jun 1, 2013

@author: Sanmaya Jolly
'''
clusters_list = []

def get_cluster(cluster_id):
    global clusters_list
    for cluster in clusters_list:
        if cluster.label == cluster_id:
            return cluster
    return None