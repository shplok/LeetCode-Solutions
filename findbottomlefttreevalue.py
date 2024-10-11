# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        
        last = 0
        q = deque([root])

        while q:
            count = len(q)
            for i in range(count):
                curr = q.popleft()
                if i == 0:
                    last = curr.val
                
                if curr.left:
                    q.append(curr.left)

                if curr.right:
                    q.append(curr.right)

        return last