#Binary search tree
class Treenode():
    def __init__(self,x):
        self.data = x
        self.left = None
        self.right = None


def InOrderTraversal(root):
    if root is not None:
        if root.left is not None:
            InOrderTraversal(root.left)
        
        print(root.data)

        if root.right is not None:
            InOrderTraversal(root.right)

def Insert(root,k):
    if root == None:
        return Treenode(k)
    if k < root.data:
        root.left = Insert(root.left,k)
    else:
        root.right = Insert(root.right,k)
    return root

def Search(root,key):
    if key == root.data:
        return root
    elif key < root.data and root.left is not None:
        return Search(root.left , key)
    elif key > root.data and root.right is not None:
        return Search(root.right , key)
    else:
        return -1
    
n = int(input("How many elements do you want in the tree?"))
root = None
for i in range(n):
    x = int(input("Enter your node value"))
    root = Insert(root , x)

InOrderTraversal(root)

key = int(input("What number do you want to search for?"))

keynode = Search(root,key)

if keynode == -1:
    print("Key is not in the tree")
else:
    print("Key is present in the tree")

    


    
         
