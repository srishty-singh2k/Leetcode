# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def checkBst(node,lVal,rVal):
            if not node:
                return True
            if lVal<node.val and node.val<rVal:
                return checkBst(node.left,lVal,node.val) and checkBst(node.right,node.val,rVal)
            else:
                return False
        return checkBst(root,float('-inf'),float('inf'))