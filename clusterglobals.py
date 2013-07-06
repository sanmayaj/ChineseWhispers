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

def replace_cluster(new_cluster, remove = False):
    global clusters_list
    for i, cluster in enumerate(clusters_list):
        if cluster.label == new_cluster.label:
            del clusters_list[i]
            if not remove:
                clusters_list.append(new_cluster)
            return
        
def print_clusters():
    global clusters_list
    s = str()
    for cluster in clusters_list:
        s += str(cluster.label) + ' '
    print s
