class Node:
    def __init__(self, data):
        self.data = data
        self.right = self.left = None


# Defining class for the Binary Tree
class NumberOfNodesInBinaryTree:
    
    
    def __init__(self): 
        self.root = None
    
    # Pre Order Traversal
    def preOrder(self, root):
        if root is None:
            return
        print(root.data, end = " ")
        self.preOrder(root.left)
        self.preOrder(root.right)

    def numNodes(self, root):
        if root is None:
            return 0
        return 1 + self.numNodes(root.left) + self.numNodes(root.right);
    
#main method
if __name__ == '__main__':
    tree = NumberOfNodesInBinaryTree()
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
    print("Number Of Nodes:", end = " ")
    print(tree.numNodes(tree.root))
