# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # max left diameter and right diameter to return to be used by upper level, then left d + right d for max diameter at this node
        return self.maxDiameter(root)[1]
    
    def maxDiameter(self, root: Optional[TreeNode]):
        if root is None:
            return (0, 0)
        left = self.maxDiameter(root.left)
        right = self.maxDiameter(root.right)
        left_only = left[0]
        right_only = right[0]
        if root.left:
            left_only = left[0]+1
        if root.right:
            right_only = right[0]+1

        return (max(left_only, right_only), max(left[1], right[1], left_only+right_only))
        
