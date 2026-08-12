# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        if not root:
            return []
        res=[]
        def tree(node):
            if node.left:
                tree(node.left)
            res.append(node.val)
            if node.right:
                tree(node.right)        
        tree(root)
        return res