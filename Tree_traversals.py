class Node:
    def __init__(self,data,left=None,right=None):
        self.left=left
        self.right=right
        self.data=data

 
def printlevel(current,d):
    if current!=None:
        if d==1:
            print(current.data)
        else:
            printlevel(current.left,d-1)
            printlevel(current.right,d-1)                 

def treeheight(t):
    if t==None:
        return 0
    else:
        leftHeight=treeheight(t.left)
        rightHeight=treeheight(t.right)
        
        if leftHeight>rightHeight:
            return leftHeight+1
        else:
            return rightHeight+1

def show(current,vtype='Inorder',stack=None):
        if current!=None and vtype=='Inorder':
            show(current.left)
            print(current.data)
            show(current.right)
        if current!=None and vtype=='Preorder':
            print(current.data)
            show(current.left, vtype='Preorder')
            show(current.right,vtype='Preorder')

        if current!=None and vtype=='Postorder':
            show(current.left, vtype='Postorder')
            show(current.right,vtype='Postorder')
            print(current.data)
            
        if current!=None and vtype=='Levelorder':
            for d in range(1,treeheight(current)+1):
                printlevel(current,d)

        if current!=None and vtype=='Inorder_stack' and stack!=None:
            show(current.left,vtype='Inorder_stack',stack=stack)
            stack.append(current.data)
            show(current.right,vtype='Inorder_stack',stack=stack)


def diameter(root):
    best={'value':1}
    def depth(root):
        if root== None: return 0
        L=depth(root.left)
        R=depth(root.right)
        best['value']=max(best['value'],L+R+1)
        return max(L,R)+1
        
    
    depth(root)
    return best['value']-1
    
    


########## 1 #########
###### 2 ######### 3 ######
### 4 ### 5 ##5.5 ## 5.6 ######
###6 7 #####################            
    
t=Node(1)
t.left=Node(2)
t.right=Node(3)

t.left.left=Node(4)
t.left.right=Node(5)

t.right.left=Node(5.5)
t.right.right=Node(5.6)


t.left.left.left=Node(6)
t.left.left.right=Node(7)

print('\nPreorder')
show(t)

print('\nPreorder')
show(t,'Preorder')

print('\nPostorder')
show(t,'Postorder')

print('\nLevelorder')
show(t,'Levelorder')

print('\nDiameter')
print(diameter(t))


print('\nInorder Stack')
s=[]
show(t,vtype='Inorder_stack',stack=s)
print(s)