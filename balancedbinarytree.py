# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def recurse(node): 
            if node is None:
                return (True, 0)
            
            lft_side, lft_height = recurse(node.left)
            rte_side, rte_height = recurse(node.right)
            

            balanced = (
                        lft_side and
                        rte_side and
                        abs(lft_height - rte_height) <= 1
                        )
            height = 1 + max(lft_height, rte_height)
            return (balanced, height)


        return recurse(root)[0]
            
