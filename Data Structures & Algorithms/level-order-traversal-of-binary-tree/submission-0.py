# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # brute force: keep track of the level number and insert into a list, go through left first then right
        return self.levelTraverse(root, 0, [])
            
    def levelTraverse(self, root: Optional[TreeNode], level: int, traversalList: List[List[int]]):
        if root is None:
            return traversalList
        if not traversalList[level:level+1]:
            traversalList.append([root.val])
        else:
            traversalList[level].append(root.val)
        traversalList = self.levelTraverse(root.left, level+1, traversalList)
        return self.levelTraverse(root.right, level+1, traversalList)
        
        
    