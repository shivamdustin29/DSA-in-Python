class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        max_depth = 0
        if root is None:
            return 0
        queue = deque([])
        queue.append(root)
        while len(queue) != 0:
            level_size = len(queue)
            for i in range(level_size):
                current = queue.popleft()
               
                
                if current.left is not None:
                    queue.append(current.left)
                if current.right is not None:
                    queue.append(current.right)
                    
                    
            max_depth += 1     
        return max_depth
