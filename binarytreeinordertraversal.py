# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # inorder implies left subtree -> curr node -> right subtree

        res = []
        def inorder(node):
            if (node):
                inorder(node.left)
                res.append(node.val)
                inorder(node.right)
        inorder(root)
        return res      
