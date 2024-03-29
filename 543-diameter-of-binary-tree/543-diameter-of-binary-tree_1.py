# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = float('-inf')
        self.dfs(root)
        return self.res
    
    def dfs(self, node):
        if not node:
            return 0
        
        left = self.dfs(node.left)
        right = self.dfs(node.right)
        
        # Using current node as root, the longest path passing through root is left + right
        # Update self.res by comparison
        self.res = max(self.res, left + right)
        
        # If return , this means this node cannot be root, it can only take one direction: max(left, right) + 1 as longest path
        return max(left, right) + 1
        
