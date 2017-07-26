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
    MAXSIZE=0
    n=0
    def __init__(self,data,SIZE):
        self.head=Node(data)
        stack.MAXSIZE=SIZE
        stack.n+=1
    
    # Push the data
    def push(self,data):
        if stack.n==stack.MAXSIZE:
            print("Stack full.")
            return 0
        else:
            newData=Node(data)
            newData.setNext(self.head)
            self.head=newData
            stack.n+=1
            return 1

    # Pull the first value
    def pull(self):
        if stack.n==0:
            print("Stack Empty.")
            return 0
        else:
            
            data=self.head.data
            self.head=self.head.getNext()
            stack.n-=1
            return data

    # Get the first value            
    def peek(self):
        if stack.n==0:
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
myStack=stack(10,6)
myStack.push(9)
myStack.push(8)
myStack.push(7)
myStack.push(6)
myStack.push(5)
myStack.push(4)

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
