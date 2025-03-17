class Treenode:
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

def Insert(root,key):
    if root is None:
        return Treenode(key)
    if root.data > key:
        root.left = Insert(root.left,key)
    if root.data < key:
        root.right = Insert(root.right,key)
    
    return root

def Delete(root,key):
    if root is None:
        return root
    if key < root.data:
        root.left = Delete(root.left,key)
    elif key > root.data:
        root.right = Delete(root.right,key) 
    else:
        #Node with no child
        if root.left is None and root.right is None:
            return None #Return None to indicate that this node should be removed
        
        #2nd Scenario = Node with one child
        elif root.left is None:
            temp = root.right
            root = None #removing the root
            return temp 
        elif root.right is None:
            temp = root.left
            root = None #removing the root 
            return temp
    
        #3rd Scenario = Node with two children
        temp = minValueNode(root.right)
        root.data = temp.data
        root.right = Delete(root.right,temp.data) 
    
    return root

def minValueNode(node):
    current = node
    while current.left is not None:
        current = current.left
    return current


num = int(input("How many numbers do you want"))       
root = None
for i in range(num):
    elements = int(input("Enter the element"))
    root = Insert(root,elements)

print("BST before deletion")
InOrderTraversal(root)

choice = int(input("What number do you want to delete"))
root = Delete(root , choice)

print("BST after deletion")
InOrderTraversal(root)


         

