# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def findPath(node, currSum):
            if node is None:
                return False
            if (node.left is None and node.right is None):
                return node.val == currSum

            left = findPath(node.left, currSum - node.val)
            right = findPath(node.right, currSum - node.val)
            return left or right

        return findPath(root, targetSum)
