class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 
class Solution: 
    def insert(self,head,data):
            p = Node(data)           
            if head==None:
                head=p
            elif head.next==None:
                head.next=p
            else:
                start=head
                while(start.next!=None):
                    start=start.next
                start.next=p
            return head  
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next

    def removeDuplicates(self,head):
        p,q = Node(None),Node(None)
        p = head
        while(p and p.next):
            if p.data == p.next.data:
                q = p.next.next
                if q == None:
                    p.next = None
                    break
                p.next = q
            else:
                p = p.next

        return head


mylist= Solution()
T=7
head=None
X = [1,1,1,1,1,1,1]
for i in range(T):
    data=X[i]
    head=mylist.insert(head,data)    
head=mylist.removeDuplicates(head)
mylist.display(head); 