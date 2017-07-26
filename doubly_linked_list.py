import numpy as np
## Doubly linked list and related operation

## Define the Node class with Data and Next variable. Functions to get and set variables
class Node:
    def __init__(self,initialValue):
        self.data = initialValue
        self.next = None
        self.pre=None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next
    
    def getPre(self):
        return self.pre

    def setData(self,newdata):
        self.data = newdata

    def setNext(self,newnext):
        self.next = newnext
    
    def setPre(self,newPre):
        self.pre = newPre
        

class doubleLinkedList:

    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def addFront(self,data):
        newNode = Node(data)
        
        if self.head==None: #if add first element
            self.head = newNode
        else: # if add to a non-empty list
            newNode.setNext(self.head)
            self.head.setPre(newNode)
            self.head = newNode
            

    def addEnd(self,data):
        newNode = Node(data)
        
        if self.head==None: #if add first element
            self.head = newNode
        else: # if add to a non-empty list
            current=self.head
            while current!=None:
                lastElement=current
                current=current.getNext()
            
            lastElement.setNext(newNode)
            newNode.setPre(lastElement)
      
    def insert(self,data,position):
        newNode = Node(data)
        
        if self.head==None: #if add to an empty list
            if position==0:
                self.head = newNode
            else:
                print("Position and list size not matched.")
        else: # if add to a non-empty list
            current=self.head
            previous=None
            n=0
            
            while n<=position:
                if n==position:
                   if position!=0: # if not the first position
                        previous.setNext(newNode)
                        newNode.setPre(previous)
                   else: # if insert at the first position
                        self.head=newNode
                        
                   newNode.setNext(current)
                   current.setPre(newNode)
                   break
                previous=current
                current=current.getNext()
                n+=1
                if current==None:
                    print("Position and list size not matched.")
                    break
                    
                        
        
        # Return list size    
    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()

        return count
    
    # Display all data as a list     
    def show(self):
        current = self.head
        values=[]
        while current != None:
            values.append(current.data)
            current = current.getNext()
            
        print values
        
myList=doubleLinkedList()
myList.addFront(14)
myList.show()

print("\nAdd three element at the front.")
myList.addFront(12)
myList.addFront(10)
myList.addFront(8)
myList.show()


print("\nAdd three element at the end.")
myList.addEnd(16)
myList.addEnd(18)
myList.addEnd(20)
myList.show()

print("\nInsert one element at the front.")
myList.insert(222,0)
myList.show()


print("\nInsert one element after 3rd position.")
myList.insert(222,3)
myList.show()

print("\nInsert one element after 6th position.")
myList.insert(222,6)
myList.show()

print("\nInsert one element out of range, 60th position.")
myList.insert(222,60)


print("\nPrint Node addresses and data from forward.")
current=myList.head;
while current!=None:
    print(id(current), current.data)
    lastElement=current
    current=current.getNext()
    
print("\nPrint Node addresses and data from backward.")
current=lastElement;
while current!=None:
    print(id(current), current.data)
    current=current.getPre()