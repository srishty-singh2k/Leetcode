# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res=[]
        #Iterative
        if not root:
            return []
        stk = [root]
        while(stk):
            node = stk.pop()
            res.append(node.val)
            if node.left:
                stk.append(node.left)
            if node.right:
                stk.append(node.right)
        return res[::-1]    

        # Recursive
        # def post(node):
        #     if not node:
        #         return
        #     if node.left:
        #         post(node.left)
        #     if node.right:
        #         post(node.right)
        #     res.append(node.val)
        # post(root)
        #return res