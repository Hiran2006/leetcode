# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def path(root,csum):
            csum+=root.val
            if not root.left and not root.right:
                if csum == targetSum:
                    return True
            else:
                if root.left and path(root.left,csum):
                    return True
                if root.right and path(root.right,csum):
                    return True
            return False
        if root:
            return path(root,0)
        return False
                
            