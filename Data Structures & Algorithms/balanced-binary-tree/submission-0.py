# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def dfs(self, node):
        if not node:
            return 0
        left = self.dfs(node.left)
        right = self.dfs(node.right)
        if abs(left - right) > 1:
            self.res = False
        return 1 + max(left, right)

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.res = True
        self.dfs(root)
        return self.res
        