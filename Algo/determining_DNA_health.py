# #!/bin/python3

# import math
# import os
# import random
# import re
# import sys

# global total_health
# total_health = 0


# class AhoCorasick:
#     def __init__(self):
#         self.goto = {}
#         self.out = []
#         self.fail = None

# def forest(genes):
#     root = AhoCorasick()

#     for i in genes:
#         node = root
#         for x in i:
#             node.goto.setdefault(x,AhoCorasick())
#         node.out.append(i)
    
#     return root

# def create_state(genes):

#     root = forest(genes)
#     queue = []

#     for i in list(root.goto.values()):
#         queue.append(i)
#         i.fail = root

#     while len(queue) > 0:
#         rnode = queue.pop(0)

#         for key,unode in list(rnode.goto.items()):
#             queue.append(unode)
#             fnode = rnode.fail
#             while fnode != None and not fnode.goto.has_key(key):
#                 fnode = fnode.fail
#             unode.fail = fnode.goto[key] if fnode else root
#             unode.out += unode.fail.out

#     return root

# def find(gh,string,root,summing_total_health):
#     node = root
#     for i in range(len(string)):
#         while node != None and string[i] in list(node.goto.keys()):
#             node = node.fail
#         if node == None:
#             node = root
#             continue
#         node = node.goto[string[i]]
#         for pattern in node.out:
#             summing_total_health(gh[pattern])
        
    
#     print(total_health)

# def summing_total_health(val):
#     total_health += val

# if __name__ == '__main__':
#     n = int(input())

#     genes = input().rstrip().split()

#     health = list(map(int, input().rstrip().split()))

#     s = int(input())

#     gh = {}
#     for x,y in zip(genes,health):
#         gh[x] = y

#     for s_itr in range(s):
#         firstLastd = input().split()

#         first = int(firstLastd[0])

#         last = int(firstLastd[1])

#         d = firstLastd[2]
#         root = create_state(genes)
#         find(gh,d,root,summing_total_health)


