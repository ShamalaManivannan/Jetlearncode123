class Treenode:
    def __init__(self, x):
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

def Insert(root, k):
    if root is None:
        return Treenode(k)
    if k < root.data:
        root.left = Insert(root.left, k)
    else:
        root.right = Insert(root.right, k)
    return root

def Search(root, key):
    if root is None:
        return -1
    if key == root.data:
        return root
    elif key < root.data:
        return Search(root.left, key)
    else:
        return Search(root.right, key)


root = None
while True:
    print("Binary Search Tree Menu:")
    print("1. Insert")
    print("2. Search")
    print("3. Display (InOrder Traversal)")
    print("4. Exit")
    
    choice = int(input("Enter your choice: "))

    if choice == 1:
        x = int(input("Enter your value to insert "))
        root = Insert(root, x)


    elif choice == 2:
        key = int(input("Enter the value to search "))
        keynode = Search(root, key)
        if keynode == -1:
            print("Key is not in the tree.")
        else:
            print("Key is present in the tree.")


    elif choice == 3:
        print("InOrder Traversal of BST")
        InOrderTraversal(root)
        


    elif choice == 4:
        print("Exiting program")
        break
    else:
        print("Invalid choice")
