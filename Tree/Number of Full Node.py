class Node:
    def __init__(self, data):
        self.data = data
        self.right = self.left = None


# Defining class for the Binary Tree
class NumberOfFullNodes:
    
   
    def __init__(self): 
        self.root = None
    
    # Pre Order Traversal
    def preOrder(self, root):
        if root is None:
            return
        print(root.data, end = " ")
        self.preOrder(root.left)
        self.preOrder(root.right)

    def numFullNodes(self, root):
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 0;
        return self.numFullNodes(root.left) + self.numFullNodes(root.right) + (1 if root.left is not None and root.right is not None else 0);
    
# main method
if __name__ == '__main__':
    tree = NumberOfFullNodes()
    tree.root = Node(1)
    tree.root.left = Node(2)
    tree.root.right = Node(3)
    tree.root.left.left = Node(4)
    tree.root.left.right = Node(5)
    tree.root.right.left = Node(6)
    tree.root.right.right = Node(7)
    print("Pre Order Traversal is:",  end = " ")
    tree.preOrder(tree.root)
    print()
    print("Number Of non-Leaf Nodes:", end = " ")
    print(tree.numFullNodes(tree.root))
