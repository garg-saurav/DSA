#Assume array elements to be from set {0,1,...,k}

def count_sort_helper(A,B,k):
    C=[]
    for i in range(k+1):
        C.append(0) 
    for x in A:
        C[x]+=1
    #C now stores frequency of elements
        
    for i in range(1,k+1):
        C[i]=C[i-1]+C[i]
    #C now stores cumulative frequency of elements
    for x in A:
        B[C[x]-1]=x
        C[x]-=1

def count_sort(A,k):
    B=[0 for x in A]
    count_sort_helper(A,B,k)
    for i in range(len(A)):
        A[i]=B[i]
    return A
