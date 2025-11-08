# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:return 0
        node = [root]
        depth=1
        while(len(node)!=0):
            for _ in range(len(node)):
                i = node.pop(0)
                if not i.left and not i.right:
                    return depth
                if i.left:
                    node.append(i.left)
                if i.right:
                    node.append(i.right)
            depth+=1
        return depth
        
