# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def preorderTraversal(self, root: TreeNode | None) -> list[int]:
        res = []

        def dfs(node):
            if not node:
                return
            res.append(node.val)  # Visit root
            dfs(node.left)        # Visit left subtree
            dfs(node.right)       # Visit right subtree

        dfs(root)
        return res