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

def show(current,type='Inorder'):
        if current!=None and type=='Inorder':
            show(current.left)
            print(current.data)
            show(current.right)
        if current!=None and type=='Preorder':
            print(current.data)
            show(current.left, type='Preorder')
            show(current.right,type='Preorder')

        if current!=None and type=='Postorder':
            show(current.left, type='Postorder')
            show(current.right,type='Postorder')
            print(current.data)
            
        if current!=None and type=='Levelorder':
            for d in range(1,treeheight(current)+1):
                printlevel(current,d)


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


show(t)
print('\n')
show(t,'Preorder')
print('\n')
show(t,'Postorder')
print('\n')
show(t,'Levelorder')
print('\n')
print(diameter(t))