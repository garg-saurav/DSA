from math import floor

def insertion_sort(A): #insertion-sort required for bucket-sort
    for i in range(1,len(A)):
        key=A[i]
        j=i-1
        while j>=0 and A[j]>key:
            A[j+1]=A[j]
            j-=1
        A[j+1]=key
    return A

def bucket_sort(A): #Assumption: All elements in [0,1) interval.
    n=len(A)
    B={}
    for i in range(n):
        if floor(n*A[i]) in B:
            B[floor(n*A[i])].append(A[i])
        else:
            B[floor(n*A[i])]=[A[i]]
    for i in B:
        insertion_sort(B[i])
    res=[]
    for i in range(n):
        if i in B:
            res=res+B[i]
    for i in range(n):
        A[i]=res[i]
    return res
        
    
