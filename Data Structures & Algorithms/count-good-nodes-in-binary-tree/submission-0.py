# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def dfs(self, node, path_max):
        if not node:
            return 
        if node.val >= path_max:
            self.res += 1
            path_max = node.val
        if node.left:
            self.dfs(node.left, path_max)
        if node.right:
            self.dfs(node.right, path_max)
        
    def goodNodes(self, root: TreeNode) -> int:
        self.res = 0
        self.dfs(root, float("-inf"))
        return self.res
        

        