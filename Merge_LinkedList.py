import numpy as np

class Node:
    def __init__(self,data=None, key=None):
        self.data=data
        self.next=key
        
class LinkedList:
    def __init__(self,data=None):
        if data==None:
            self.head=None
        else:
            self.head=Node(data)
            
    def __repr__(self):
         return 'LinkedList: %d'%len(self.show())
    
    def add(self,data):
        newNode=Node(data,self.head)
        self.head=newNode
        
    def push(self,data):
        if self.head==None:
            self.head=Node(data)
            return
        else:
            c=self.head
            
        while c.next!=None:
            c=c.next
        c.next=Node(data)
                
    
    def addArray(self,a):
        a=a[::-1]
        for i in a:
            self.add(i)
    
    def show(self):
        if self.head==None:
            print("Empty List.")
            return
        else:
            current=self.head
        
        data=[]
        while current:
            data.append(current.data)
            current=current.next
        print(data)
        return data 
    def reverse(self):
        if self.head==None:
            print("Empty List.")
            return
        else:
            prev=None
            current=self.head
            
        while current:
            nextnode=current.next
            current.next=prev
            
            prev=current
            current=nextnode
        self.head=prev


def mergeLinkedList(la,lb):
    if la.head==None and lb.head==None:
        c=LinkedList()
    elif la.head==None and lb.head!=None:
        return lb
    elif la.head!=None and lb.head==None:
        return la
    else:
        a=la.head
        b=lb.head
        c=LinkedList()
    
    
    while a!=None and b!=None:
        if a.data<b.data:
            c.add(a.data)
            a=a.next
            continue
        if b.data<a.data:
            c.add(b.data)
            b=b.next
            continue
        if a.data==b.data:
            c.add(a.data)
            c.add(b.data)
            a=a.next
            b=b.next
    
    
    while a!=None:
        c.add(a.data)
        a=a.next
    while b!=None:
        c.add(b.data)
        b=b.next
    
    c.reverse() 
    return c 


############# Main function ###############
N=np.random.randint(5,20,1)
a=np.random.randint(1,100,N)
a.sort()
N=np.random.randint(5,20,1)
b=np.random.randint(1,100,N)
b.sort()

# Create two linkedlist from two array
la=LinkedList()
lb=LinkedList()
la.addArray(a)
lb.addArray(b)

la.show()
lb.show()

# Merge linked list
lc=mergeLinkedList(la,lb)
lc.show()    

