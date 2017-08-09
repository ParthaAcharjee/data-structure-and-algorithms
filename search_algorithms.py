import numpy as np
# In this simple demo, we'll implement linear, binary, and interpolation search
# method. We will count the number of comparison for each methods.

def linear_search(a,target,N):
    
    for i in range(N):
        if a[i]==target:
            return i,i+1         
    return None,i+1

    
def binary_search(a,target,N):
    low=0
    high=N-1
    mid=int((low+high)/2)
    sortedIndex=np.argsort(a)
    asorted=a[sortedIndex]
    k=0
    while asorted[mid]!=target:
        k+=1
        if high<low:
            return None,k
        mid=low+int((high-low)*0.5)
        
        if asorted[mid]<target:
            low=mid+1
        elif asorted[mid]>target:
            high=mid-1
        
    return sortedIndex[mid],k

        
def interpolation_search(a,target,N):
   
    low=0
    high=N-1
    mid=int((low+high)/2)
    sortedIndex=np.argsort(a)
    asorted=a[sortedIndex]
    k=0
    while asorted[mid]!=target:
        k+=1
        if high<=low or asorted[high]<=asorted[low]:
            return None,k
            
        c=(target-asorted[low])/(asorted[high]-asorted[low])
        mid=low+int((high-low)*c)
        
        if asorted[mid]<target:
            low=mid+1
        elif asorted[mid]>target:
            high=mid-1
        
    return sortedIndex[mid],k
                
                                
                
def generate_data(N):
    a=np.random.rand(N)
    np.random.shuffle(a)
    target=a[int(N*np.random.rand())]
    return a,target

    
            
N=10000
run=10
linear_count=0
binary_count=0
interpolation_count=0

linear_indx=0
binary_indx=0
interpolation_indx=0


for i in range(run):
    a,target=generate_data(N)
    
    indx,countNew=linear_search(a,target,N)
    linear_count+=countNew
    linear_indx+=indx
    
    indx,countNew=binary_search(a,target,N)
    binary_count+=countNew
    binary_indx+=indx
    
    indx,countNew=interpolation_search(a,target,N)
    interpolation_count+=countNew
    interpolation_indx+=indx


print("       (Linear) Index sum: %d Comparison count: %d"%(linear_indx,linear_count))
print("       (Binary) Index sum: %d Comparison count: %d"%(binary_indx,binary_count))
print("(Interpolation) Index sum: %d Comparison count: %d"%(interpolation_indx,interpolation_count))

    
        
