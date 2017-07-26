class Node:

    def __init__(self,data):
        self.data=data
        self.next=None
    def getData(self):
        return self.data
    def getNext(self):
        return self.next
    def setData(self,newData):
        self.data=newData
    def setNext(self,newNext):
        self.next=newNext


class stack:

    def __init__(self,SIZE):
        self.head=None
        self.MAXSIZE=SIZE
        self.n=0
        
    # Push the data
    def push(self,data):
        if self.n==self.MAXSIZE:
            print("Stack full.")
            return 0
        else:
            newData=Node(data)
            if self.head!=None:
                newData.setNext(self.head)
            self.head=newData
            self.n+=1
            return 1

    # Pull the first value
    def pull(self):
        if self.n==0:
            print("Stack Empty.")
            return 0
        else:
            
            data=self.head.data
            self.head=self.head.getNext()
            self.n-=1
            return data

    # Get the first value            
    def peek(self):
        if self.n==0:
            print("Stack Empty.")
            return 0
        else:
            return self.head.data
            
    # Display all data as a list     
    def show(self):
        current = self.head
        values=[]
        while current != None:
            values.append(current.data)
            current = current.getNext()
            
        print(values)

print("\nCreate a stack. (Push 7 values in a 6 maxsize stack.)")
myStack=stack(6)
myStack.push(9)
myStack.push(8)
myStack.push(7)
myStack.push(6)
myStack.push(5)
myStack.push(4)
myStack.push(3)

myStack.show()

print("\nPull the first value: ",myStack.pull())
myStack.show()
print("\nPull the first value: ",myStack.pull())
myStack.show()
print("\nPull the first value: ",myStack.pull())
myStack.show()
print("\nPull the first value: ",myStack.pull())
myStack.show()


print("\nPeek the first value: ",myStack.peek())
myStack.show()
