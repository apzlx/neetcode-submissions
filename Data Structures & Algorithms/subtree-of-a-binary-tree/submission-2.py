# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        if root is None and subRoot is None:
            return True  
        elif root is None or subRoot is None:
            return False

        if root.val == subRoot.val:
            if self.isSameTree(root.left, subRoot.left) and self.isSameTree(root.right, subRoot.right):
                return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
    
    def isSameTree(self, aTree: Optional[TreeNode], bTree: Optional[TreeNode]):
        if aTree is None and bTree is None:
            return True
        
        if aTree and bTree and aTree.val == bTree.val:
            return self.isSameTree(aTree.left, bTree.left) and self.isSameTree(aTree.right, bTree.right)
        return False
        