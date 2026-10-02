# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def dfs(self, node, low, upper):
        if not node:
            return True
        if node.val <= low or node.val >= upper:
            return False 

        left = self.dfs(node.left, low, node.val)
        right = self.dfs(node.right, node.val, upper)
        return left and right
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.dfs(root, float("-inf"), float("inf"))

        