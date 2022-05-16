# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
          """
        if len(inorder)==0 or len(postorder)==0:
            return None
			
        tree_len = len(postorder)
        root = TreeNode(postorder[tree_len -1])
        mid = inorder.index(postorder[tree_len -1])
		
        root.left = self.buildTree(inorder[:mid], postorder[0:mid])
        root.right = self.buildTree(inorder[mid+1:], postorder[mid:tree_len -1])
        
        return root
