from stack_using_linkedList import stack
# Dequeue and enqueue of a queue using two stacks

class queue:
    MAXSIZE=0
    size=0
    def __init__(self,MAXSIZE):
        queue.MAXSIZE=MAXSIZE
        
        self.mainStack=stack(MAXSIZE)
        self.tempStack=stack(MAXSIZE)
    
    def enqueue(self,data):
        if queue.size<queue.MAXSIZE:
            self.mainStack.push(data)
            queue.size+=1
        else:
            print("Queue full.")
        
    def dequeue(self):
        if queue.size>0:
            while self.mainStack.n>0:
                self.tempStack.push(self.mainStack.pull())
            
            data=self.tempStack.pull()
            while self.tempStack.n>0:
                self.mainStack.push(self.tempStack.pull())
            return data
        else:
            print("Queue Empty.")
            return 0
 
        
    def show(self):
        self.mainStack.show()

print("\nEnqueue elements in a 6-MAXSIZE queue.")
N=6
Q=queue(N)

data=[10,20,30,40,50,60,70,80,90]
print("Data to enqueue in the queue: ",data)
for i in data:
    Q.enqueue(i)
    Q.show()

print("\n\nStart dequeue from the queue")
for i in range(N):
    print(Q.dequeue())
    Q.show()