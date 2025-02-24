class Treenode():
    def __init__(self,data):
        self.data  = data
        self.leftnode= None
        self.rightnode = None

def in_order_traversal(root):
    if root.leftnode != None:
        in_order_traversal(root.leftnode)

    print(root.data)
    
    if root.rightnode != None:
        in_order_traversal(root.rightnode)
    
def pre_order_traversal(root):
    
    print(root.data)

    if root.leftnode != None:
        pre_order_traversal(root.leftnode)

    if root.rightnode != None:
        pre_order_traversal(root.rightnode)   

def post_order_traversal(root):

    if root.leftnode != None:
        post_order_traversal(root.leftnode)

    if root.rightnode != None:
        post_order_traversal(root.rightnode)

    print(root.data)

root = Treenode(5)
root.leftnode = Treenode(4)
root.leftnode.leftnode = Treenode(2)        

root.rightnode = Treenode(8)
root.rightnode.leftnode = Treenode(7)
root.rightnode.rightnode = Treenode(9)

in_order_traversal(root)
pre_order_traversal(root)
post_order_traversal(root)
