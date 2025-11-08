# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def checkBalance(root):
            if not root:
                return 0
            left = checkBalance(root.left)
            right = checkBalance(root.right)

            if right == -1 or left ==-1:
                return -1
            diff = abs(right-left)
            if diff>1:
                return -1
            else:
                return max(left,right)+1
        return checkBalance(root)!=-1
            

        
