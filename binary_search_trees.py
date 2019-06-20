#test=bst()
#Available functions for complete tree:
    #test.inorder_tree_walk()
    #test.tree_insert(key)
    #test.tree_search(key)
    #test.tree_min()
    #test.tree_max()
    #test.tree_delete(node)

#nod=test.tree_search(some_key)
#Available functions for a node:
    #nod.tree_search(key)       #for searching in the subtree with nod as root
    #nod.tree_min()             #minimum key node in the subtree with nod as root
    #nod.tree_max()             #maximum key node in the subtree with nod as root
    #nod.inorder_tree_walk()    #sorted order of keys in the subtree with nod as root
    #nod.tree_successor()
    #nod.tree_predecessor()
    


class nil_node:
    def __init__(self):
        self.key=None
        self.parent=None
        self.left=None
        self.right=None

NIL = nil_node()

class node:
    def __init__(self,key,parent,left=NIL,right=NIL):
        self.key=key
        self.parent=parent
        self.left=left
        self.right=right

    def tree_search(self,key): #takes key as argument and returns corresponding node
        T=self
        while T!=NIL and key!=T.key:
            if key<T.key:
                T=T.left
            else:
                T=T.right
        return T

    def tree_min(self): #takes root-node as argument and returns min node
        T=self
        while T.left!=NIL:
            T=T.left
        return T

    def tree_max(self): #takes root-node as argument and returns min node
        T=self
        while T.right!=NIL:
            T=T.right
        return T
    
    def inorder_tree_walk(self):
        if self.left!=NIL:
            self.left.inorder_tree_walk()
        print(self.key,end=' ')
        if self.right!=NIL:
            self.right.inorder_tree_walk()

    def tree_successor(self): #takes node as an argument and returns node
        T=self
        if T.right!=NIL:
            return T.right.tree_min()
        else:
            while T.parent!=NIL and T!=T.parent.left:
                T=T.parent
            return T.parent

    def tree_predecessor(self): #takes node as an argument and returns node
        T=self
        if T.left!=NIL:
            return T.left.tree_max()
        else:
            while T.parent!=NIL and T!=T.parent.right:
                T=T.parent
            return T.parent

class bst: 

    def __init__(self):
        self.root=NIL
        
    def inorder_tree_walk(self):
        T=self.root
        T.inorder_tree_walk()

    def tree_search(self,key):
        T=self.root
        return T.tree_search(key)

    def tree_min(self): 
        T=self.root
        return T.tree_min()

    def tree_max(self):
        T=self.root
        return T.tree_max()
    
    def tree_insert(self,key): #takes key to be added as argument
        parent=NIL
        T=self.root
        while T!=NIL:
            parent=T
            if key<=T.key:
                T=T.left
            else:
                T=T.right
        new_node=node(key,parent)
        if parent==NIL:
            self.root=new_node
        elif key<=parent.key:
            parent.left=new_node
        else:
            parent.right=new_node
            

    def tree_delete(self,nod): #takes node to be deleted as an argument
        if nod==self.root: #node has NIL as parent
            if nod.left==NIL and nod.right==NIL:
                self.root=NIL
            elif nod.left==NIL:
                self.root=nod.right
                self.root.parent=NIL
            elif nod.right==NIL:
                self.root=nod.left
                self.root.parent=NIL
            else:
                new_root=nod.tree_successor()
                self.tree_delete(new_root)
                self.root=new_root
                new_root.parent=NIL
                new_root.left=nod.left
                new_root.right=nod.right
                nod.left.parent=new_root
                nod.right.parent=new_root
        else:
            if nod is nod.parent.left: #node to be deleted is left child of its parent
                if nod.left==NIL and nod.right==NIL: #node has no children
                    nod.parent.left=NIL
                elif nod.left==NIL: #node has only right child
                    nod.parent.left=nod.right
                    nod.right.parent=nod.parent
                elif nod.right==NIL: #node has only left child
                    nod.parent.left=nod.left
                    nod.left.parent=nod.parent
                else: #node has both children
                    new_root=nod.tree_successor() 
                    self.tree_delete(new_root)
                    nod.parent.left=new_root
                    new_root.parent=nod.parent
                    new_root.left=nod.left
                    new_root.right=nod.right
                    nod.left.parent=new_root
                    nod.right.parent=new_root
            else:  #node to be deleted is right child of its parent
                if nod.left==NIL and nod.right==NIL: #node has no children
                    nod.parent.right=NIL
                elif nod.left==NIL: #node has only right child
                    nod.parent.right=nod.right
                    nod.right.parent=nod.parent
                elif nod.right==NIL: #node has only left child
                    nod.parent.right=nod.left
                    nod.left.parent=nod.parent
                else: #node has both children
                    new_root=nod.tree_successor()
                    self.tree_delete(new_root)
                    nod.parent.right=new_root
                    new_root.parent=nod.parent
                    new_root.left=nod.left
                    new_root.right=nod.right
                    nod.left.parent=new_root
                    nod.right.parent=new_root
                    
                    

                    
                
            
            
            
            
        
        
    
            
            
        
        
