from random import randrange

def swap(A,i,j):
    temp=A[i]
    A[i]=A[j]
    A[j]=temp

def randomized_partition(A,p,r):
    i=randrange(p,r+1,1)
    swap(A,r,i)
    x=A[r] #random pivot
    i=p-1
    for j in range(p,r):
        if A[j]<=x:
            i+=1
            swap(A,j,i)
    swap(A,i+1,r)
    return i+1

def randomized_select_helper(A,p,r,i): #returns i-th smallest element of A[p]...A[r]
    if p==r:
        return A[p]
    q=randomized_partition(A,p,r)
    #A[0]...A[q-1] : Elements <= pivot
    #A[q] : pivot
    #A[q+1]...A[r] : Elements >= pivot
    
    k=q-p+1 #pivot is k-th smallest element of array A[p]...A[r]
    if i==k:
        return A[q]
    elif i<k:
        return randomized_select_helper(A,p,q-1,i)
    else: #i>k
        return randomized_select_helper(A,q+1,r,i-k)

def randomized_select(A,i):
    return randomized_select_helper(A,0,len(A)-1,i)
