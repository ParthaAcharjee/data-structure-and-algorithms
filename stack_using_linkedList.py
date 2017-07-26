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

    # Display all data as a list     
    def show(self):
        current = self.head
        values=[]
        while current != None:
            values.append(current.data)
            current = current.getNext()
            
        print(values)

myStack=stack(10,5)
myStack.push(1)
myStack.push(2)
myStack.push(3)
myStack.push(4)
myStack.push(5)
myStack.push(6)

myStack.show()