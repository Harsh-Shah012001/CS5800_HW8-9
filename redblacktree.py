class Node:
    def __init__(self,data):
        self.data=data 
        self.color='Red'
        self.lchild=None
        self.rchild=None
        self.parent=None

class RedBlackTree:
    root=Node(None)
    NIL=Node(None)
    pre = None
    suc = None
    def __init__(self) -> None:
        self.NIL = Node(0)
        self.NIL.color = "BLACK"
        self.NIL.lchild = self.NIL.rchild = self.NIL
        self.root = self.NIL


    def leftRotate(self,x):
        y=x.rchild
        x.rchild=y.lchild
        if(y.lchild!=self.NIL):
            y.lchild.parent=x
        y.parent=x.parent
        if(x.parent==None):
            self.root=y
        elif(x==x.parent.lchild):
            x.parent.lchild=y
        else:
            x.parent.rchild=y
        y.lchild=x
        x.parent=y
    
    def rightRotate(self,x):
        y=x.lchild
        x.lchild=y.rchild
        if(y.rchild!=self.NIL):
            y.rchild.parent=x
        y.parent=x.parent
        if(x.parent==None):
            self.root=y
        elif(x==x.parent.rchild):
            x.parent.rchild=y
        else:
            x.parent.lchild=y
        y.rchild=x
        x.parent=y
    
    def fixInsert(self,k):
        while(k!=self.root and k.parent.color=='Red'):
            if(k.parent==k.parent.parent.lchild):
                u=k.parent.parent.rchild #Uncle
                if(u.color=='Red'):
                    k.parent.color='Black'
                    u.color='Black'
                    k.parent.parent.color='Red'
                    k=k.parent.parent
                else:
                    if(k==k.parent.rchild):
                        k=k.parent
                        self.leftRotate(k)
                    k.parent.color='Black'
                    k.parent.parent.color='Red'
                    self.rightRotate(k.parent.parent)
            else:
                u=k.parent.parent.lchild
                if(u.color=='Red'):
                    k.parent.color='Black'
                    u.color='Black'
                    k.parent.parent.color='Red'
                    k=k.parent.parent
                else:
                    if(k==k.parent.lchild):
                        k=k.parent
                        self.rightRotate(k)
                    k.parent.color='Black'
                    k.parent.parent.color='Red'
                    self.leftRotate(k.parent.parent)
        self.root.color='Black'

    def insert(self,data):
        newNode=Node(data)
        newNode.lchild=self.NIL
        newNode.rchild=self.NIL

        curr=self.root
        parent=None

        while(curr!=self.NIL):
            parent=curr
            if(newNode.data<curr.data):
                curr=curr.lchild
            else:
                curr=curr.rchild
        newNode.parent=parent
        if(parent==None):
            self.root=newNode
        elif(newNode.data<parent.data):
            parent.lchild=newNode
        else:
            parent.rchild=newNode

        if(newNode.parent==None):
            newNode.color="Black"
            return
        if(newNode.parent.parent==None):
            return
        self.fixInsert(newNode)
    
    def inorder(self):
        self.inorderHelper(self.root)

    def inorderHelper(self,node):
        if(node!=self.NIL):
            self.inorderHelper(node.lchild)
            print(node.data,end=" ")
            self.inorderHelper(node.rchild)
    
    def search(self,data):
        res= self.searchHelper(self.root,data)
        if(res==self.NIL or res==None):
            return "Not Found"
        else:
            return "Found"
    def searchHelper(self,node,data):
        if(node==self.NIL or data==node.data):
            return node
        elif(data<node.data):
            return self.searchHelper(node.lchild,data)
        else:
            return self.searchHelper(node.rchild,data)

    def findPreSuc(self, root, key):
        if root==self.NIL:
            return
    
        # If key is present at root
        if root.data == key:
            if root.lchild != self.NIL:
                tmp = root.lchild 
                while(tmp.rchild!=self.NIL):
                    tmp = tmp.rchild 
                self.pre = tmp
    
            if root.rchild != self.NIL:
                tmp = root.rchild
                while(tmp.lchild!=self.NIL):
                    tmp = tmp.lchild 
                self.suc = tmp 
            return
        if root.data > key :
            self.suc = root 
            self.findPreSuc(root.lchild, key)
        else:
            self.pre = root
            self.findPreSuc(root.rchild, key)
    
    def PredSuc(self,key):
        
        self.findPreSuc(self.root, key)
        
        if self.pre is not None:
            print("Predecessor is", self.pre.data)
        
        else:
            print ("No Predecessor")
        
        if self.suc is not None:
            print ("Successor is", self.suc.data)
        else:
            print ("No Successor")

    def findMax(self,node):
        if (node == self.NIL):
            return float('-inf')
        res = node.data
        lres = self.findMax(node.lchild)
        rres = self.findMax(node.rchild)
        if (lres > res):
            res = lres
        if (rres > res):
            res = rres
        return res
    
    def Max(self):
        return self.findMax(self.root)
    
    def Min(self):
        return self.findMin(self.root)
    
    def findMin(self,node):
        if node==self.NIL:
            return float('inf')
        res = node.data
        lres = self.findMin(node.lchild)
        rres = self.findMin(node.rchild)
        if lres < res:
            res = lres
        if rres < res:
            res = rres
        return res
    
    def deleteNode(self,key):
        self.root= self.delete(self.root,key)

    def delete(self,node,key):
        if(node==self.NIL or node is None):
            return None
        if(key<node.data):
            node.lchild=self.delete(node.lchild,key)
        elif(key>node.data):
            node.rchild=self.delete(node.rchild,key)
        else:
            if node.lchild == self.NIL:
                return node.rchild
            elif node.rchild == self.NIL:
                return node.lchild
            node.data = self.minValue(node.rchild)
            # Delete the inorder successor
            node.rchild = self.delete(node.rchild, node.data)
        return node
    
    def minValue(self, node):
        minv = node.data
        while node.lchild!=self.NIL:
            minv = node.lchild.data
            node = node.lchild
        return minv
    
    def height(self,node):
        if node is None or node==self.NIL:
            return 0
        else:
            lDepth = self.height(node.lchild)
            rDepth = self.height(node.rchild)    
            if (lDepth > rDepth):
                return lDepth+1
            else:
                return rDepth+1
    
    def findHeight(self):
        return self.height(self.root)

rbt=RedBlackTree()

file_path = 'input.txt'
with open("F:\MS in CS\Algorithms\HW8\RedBlackTree\input.txt", 'r', encoding='ISO-8859-1') as file:
    text = file.read()
data=text.split('\n')

for i in data:
    rbt.insert((int)(i))

while(True):
    print("\n1. Insert \n2. Delete\n3. Minimum\n4. Maximum\n5. Predecessor & Successor\n6. Sort\n7. Search\n8. Exit")
    ch=input("Select an operation: ")
    if(ch=='1'):
        n=int(input("Enter node to be inserted: "))
        rbt.insert(n)
        print("Height of tree is: ",rbt.findHeight())
    elif(ch=='2'):
        n=int(input("Enter node to be deleted: "))
        rbt.deleteNode(n)
        print("Height of tree is: ",rbt.findHeight)
    elif(ch=='3'):
        print("Minimum: ",rbt.Min())
    elif(ch=='4'):
        print("Maximum: ",rbt.Max())
    elif(ch=='5'):
        n=int(input("Enter node for which Pred/Suc is required: "))
        rbt.PredSuc(n)
    elif(ch=='6'):
        rbt.inorder()
    elif(ch=='7'):
        n=int(input("Enter node to be searched: "))
        print(rbt.search(n))
    elif(ch=='8'):
        print('Thank you')
        break
    else:
        print("Invalid")
'''
rbt.insert(10)
rbt.insert(20)
rbt.insert(30)
rbt.insert(15)

print("Sorted order: ")
rbt.inorder()
print()
print("Maximum: ",rbt.Max())
print("Minimum: ",rbt.Min())
rbt.PredSuc(15)
print("*********************")
print(rbt.deleteNode(10))
rbt.inorder()
'''