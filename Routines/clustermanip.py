'''
Created on Apr 3, 2013

@author: Sanmaya Jolly
'''

import random

def random_cluster(li):
    length = len(li)
    x = random.randint(0, length - 1)
    return li[x]