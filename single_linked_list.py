import numpy as np
## Singly linked list and related operation

## Define the Node class with Data and Next variable. Functions to get and set variables
class Node:
    def __init__(self,initialValue):
        self.data = initialValue
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self,newdata):
        self.data = newdata

    def setNext(self,newnext):
        self.next = newnext
        
        
class UnorderedList:

    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def addFront(self,data):
        newNode = Node(data)
        newNode.setNext(self.head)
        self.head = newNode

    def addEnd(self,data):
        current=self.head
        while current!=None:
            previous=current;
            current=current.getNext()
       
        newNode = Node(data)
        previous.setNext(newNode)
   
    def insert(self,data,position):
        #Insert in front if postion less then 1, Insert at end if position greater than size
        if position<1:
            self.addFront(data)
            return
        if position>self.size():
            self.addEnd(data)
            return
            
        # Insert data at given position    
        newNode = Node(data)        
        current=self.head
        for i in range(position):
            previous=current
            current=current.getNext()
            
        previous.setNext(newNode)
        newNode.setNext(current)
    
    def delete(self,position):
        if position>=self.size():
            return;
            
        current=self.head
        previous=None
        
        for i in range(position):
            previous=current
            current=current.getNext()
         
        if previous==None:
            self.head=current.getNext()
        elif current==None:
            print "none"
        else:
            previous.setNext(current.getNext())     
                
        
    
    
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
            
                      
myList=UnorderedList();

myList.addFront(60)
myList.addFront(55)
myList.addFront(50)
myList.addFront(45)
myList.addEnd(75)
myList.addEnd(80)

print("\nInitial list")
myList.show()

print("\nDelete 11th element")
myList.delete(10)
myList.show()

print("\nDelete 6th element")
myList.delete(5)
myList.show()


print("\nDelete 3rd element")
myList.delete(2)
myList.show()

print("\nInset 2nd element")
myList.insert(2222,1)
myList.show()

print("\nDelete 1st element")
myList.delete(0)
myList.show()