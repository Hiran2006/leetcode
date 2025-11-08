# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        def mind(root):
            if not root:
                return 0
            
            if not root.left and not root.right:
                return 1
            left= mind(root.left)
            right = mind(root.right)
            if left ==0:
                return right+1
            if right == 0:
                return left+1
            return min(left,right)+1
        return mind(root)
