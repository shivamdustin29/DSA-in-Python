# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if len(nums)==0:
            return None
        middleIndex = len(nums)//2
        returnNode = TreeNode(nums[middleIndex])
        returnNode.left=self.sortedArrayToBST(nums[:middleIndex])
        returnNode.right=self.sortedArrayToBST(nums[middleIndex+1:])
        return returnNode
