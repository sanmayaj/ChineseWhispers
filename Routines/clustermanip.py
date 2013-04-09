'''
Created on Apr 3, 2013

@author: Sanmaya Jolly
'''

import random

def random_cluster(li):
    length = len(li)
    if length > 1:
        x = random.randint(0, length - 1)
        return li[x]
    elif length == 1:
        return li[0]
    if li == []:
        return None