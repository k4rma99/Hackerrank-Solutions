import sys

class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root

    def levelOrder(self,root):
        q = []
        if root:
            q.append(root)
        
        while len(q)!=0:
            current_head = q.pop(0)
            print(current_head.data,end = " ")
            if current_head.left:
                q.append(current_head.left)
            if current_head.right:    
                q.append(current_head.right)

T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
myTree.levelOrder(root)
