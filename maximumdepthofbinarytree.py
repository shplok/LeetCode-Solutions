# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        max_depth = 0
        depth = 0
        def inorder(node, depth):
            nonlocal max_depth
            max_depth = max(max_depth, depth)
            if (node):         
                inorder(node.left, depth + 1)
                inorder(node.right, depth + 1)

        inorder(root, depth)
        return max_depth
