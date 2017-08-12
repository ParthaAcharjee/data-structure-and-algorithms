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
            
         

A=LinkedList()
for i in range(10):
    A.add(i)
    

A.show()
A.reverse()
A.show()
        