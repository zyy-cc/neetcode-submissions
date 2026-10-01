# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution: 

    def sameTree(self, node1, node2):
        if not node1 and not node2:
            return True
        if not node1 or not node2:
            return False 
        if node1.val != node2.val:
            return False
        else:
            return self.sameTree(node1.left, node2.left) and self.sameTree(node1.right, node2.right)
           
    def dfs(self, node, subnode):
        if not node:
            return False
        if self.sameTree(node, subnode):
            return True
        return self.dfs(node.left, subnode) or self.dfs(node.right, subnode)

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        return self.dfs(root, subRoot)
        