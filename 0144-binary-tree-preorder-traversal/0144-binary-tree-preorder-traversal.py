# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res=[]
        #Iterative
        # if not root:
        #     return []
        # stk = [root]
        # while(stk):
        #     node = stk.pop()
        #     res.append(node.val)
        #     if node.right:
        #         stk.append(node.right)
        #     if node.left:
        #         stk.append(node.left)
        
        # Recursive
        def pre(node):
            if not node:
                return
            res.append(node.val)
            pre(node.left)
            pre(node.right)
        pre(root)
        return res