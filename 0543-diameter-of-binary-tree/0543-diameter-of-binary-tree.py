# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        maxdia = 0
        def post(node):
            nonlocal maxdia
            if not node:
                return 0
            l = post(node.left)
            r = post(node.right)
            maxdia = max(maxdia,l+r)
            return max(l,r)+1
        post(root)
        return maxdia
