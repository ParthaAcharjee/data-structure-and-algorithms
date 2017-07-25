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
myList.addFront(12)
myList.addFront(10)
myList.addFront(8)

myList.show()

myList.addEnd(16)
myList.addEnd(18)
myList.addEnd(20)

myList.show()