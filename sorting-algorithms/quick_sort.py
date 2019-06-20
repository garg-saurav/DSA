def swap(A,i,j):
    temp=A[i]
    A[i]=A[j]
    A[j]=temp

def partition(A,p,r):
    pivot=A[r]
    i=p-1
    for j in range(p,r): #A[p]...A[i]<=pivot and A[i+1]...A[j-1]>pivot
        if A[j]<=pivot:
            i+=1
            swap(A,i,j)
    swap(A,i+1,r) #now A[i+1] is pivot
    return i+1

def qsort_helper(A,p,r):
    if p<r:
        q=partition(A,p,r)
        qsort_helper(A,p,q-1)
        qsort_helper(A,q+1,r)

def quick_sort(A):
    qsort_helper(A,0,len(A)-1)
    return A
    
