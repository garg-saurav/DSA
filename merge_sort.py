def merge(A,p,q,r):
    n1=q-p+1
    n2=r-q
    L=[] #for storing left half A[p]...A[q]
    R=[] #for storing right half A[q+1]...A[r]
    for i in range(n1):
        L.append(A[p+i])
    for j in range(n2):
        R.append(A[q+j+1])
    i=j=0
    k=p
    while i<n1 and j<n2:
        if L[i]<=R[j]:
            A[k]=L[i]
            i+=1
            k+=1
        else:
            A[k]=R[j]
            j+=1
            k+=1
    if i>n1: #elements remain in R[j]...R[n2-1]
        for t in range(j,n2):
            A[k]=R[t]
            k+=1
    else: #elements remain in L[i]...L[n1-1]
        for t in range(i,n1):
            A[k]=L[t]
            k+=1

def merge_sort_helper(A,p,r):
    if p<r:
        q=(p+r)//2
        merge_sort_helper(A,p,q)
        merge_sort_helper(A,q+1,r)
        merge(A,p,q,r)

def merge_sort(A):
    merge_sort_helper(A,0,len(A)-1)
    return A
    
            
