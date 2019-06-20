def left(i):
    return 2*i

def right(i):
    return 2*i+1

def parent(i):
    return i//2

def swap(A,i,j):
    temp=A[i]
    A[i]=A[j]
    A[j]=temp
    
class heap:
    def max_heapify(self, i): 
        
        #It makes self.elements satisfy the max_heap property for node at 
        #index i assuming its left and right child already satisfy it
        
        if (i==0):
            print('Invalid index of heap accessed')
            return
        largest=0
        A=[]
        A=self.elements
        S=self.heap_size
        while True:
            l=left(i)
            r=right(i)
            if l<=S and A[i]<A[l]:
                largest=l
            else:
                largest=i
            if r<=S and A[largest]<A[r]:
                largest=r
            if largest==i:
                return
            else:
                swap(A,largest,i)
                i=largest
            
    def build_max_heap(self):
        for i in range(self.heap_size//2, 0, -1):
            self.max_heapify(i)
        
    def add_elements(self, B): #this function itself ensures the heap property
        for x in B:
            self.elements.append(x)
            self.heap_size+=1
        self.build_max_heap()
        
    def __init__(self,B=[]):
        self.elements=[0]
        self.heap_size=0
        self.add_elements(B)
        
def heap_sort(A):
    temp=heap()
    temp.add_elements(A) #now temp has heap containing elements of A
    for i in range(len(temp.elements)-1,0,-1):
        swap(temp.elements,1,i)
        A[i-1]=temp.elements[i]
        temp.heap_size-=1
        temp.max_heapify(1)
    return A
    





    


                                    
    
