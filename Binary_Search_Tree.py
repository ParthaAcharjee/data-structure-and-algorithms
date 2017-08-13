class Node:
    def __init__(self,data,left=None,right=None):
        self.left=left
        self.right=right
        self.data=data


class bst:  
    def __init__(self):
        self.root=None
    
    def add(self,data):
        
        def addElement(currentNode,data):
            if currentNode.data<data:
                if currentNode.right!=None: addElement(currentNode.right,data)
                else: currentNode.right=Node(data)
            if currentNode.data>data:
                if currentNode.left==None: currentNode.left=Node(data) 
                else: addElement(currentNode.left,data)
        
        
        if self.root==None: self.root=Node(data)
        else:
            addElement(self.root,data)
    
    def show(self,ttype='Inorder'):
        current=self.root
        if ttype=='Inorder':
            def inorder(node,stack):
                if node:
                    inorder(node.left,stack)
                    stack.append(node.data)
                    inorder(node.right,stack)
                    
            
            stack=[]; inorder(current,stack); print(stack)
            
        if ttype=='Levelorder':
            
            def height(current):
                if current==None: return 0
                else:
                    L=height(current.left)
                    R=height(current.right)
                    if L>R: return L+1
                    else: return R+1
                    
            
            def printlevel(current,d,stack):
                if current:
                    if d==1:  stack.append(current.data)
                    else: 
                        printlevel(current.left,d-1,stack)
                        printlevel(current.right,d-1,stack)
            
            for d in range(1,height(current)+1):
                stack=[]
                printlevel(current,d,stack)
                print(stack)
            


t=bst()
t.add(50)
t.add(40); t.add(60)
t.add(30); t.add(45); t.add(55); t.add(70)
t.add(20); t.add(35); t.add(42); t.add(48); t.add(52); t.add(58); t.add(68); t.add(72)


print('\nLevelorder show:')
t.show('Levelorder')
print('\nInorder show:')
t.show()