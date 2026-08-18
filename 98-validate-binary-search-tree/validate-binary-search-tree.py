# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(node, low=float('-inf'), high=float('inf')):
            if not node:
                return True
            
            # The current node's value must strictly satisfy: low < node.val < high
            if not (low < node.val < high):
                return False
            
            # Left subtree must have values strictly less than node.val
            # Right subtree must have values strictly greater than node.val
            return validate(node.left, low, node.val) and validate(node.right, node.val, high)

        return validate(root)