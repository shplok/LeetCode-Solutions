from collections import deque

class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        max_width = 0
        queue = deque([(root, 0)])  # (node, index)

        while queue:
            level_length = len(queue)
            _, first_index = queue[0]
            for i in range(level_length):
                node, index = queue.popleft()
                # Normalize index to prevent overflow
                index -= first_index
                if i == 0:
                    level_start = index
                if i == level_length - 1:
                    level_end = index
                if node.left:
                    queue.append((node.left, 2 * index))
                if node.right:
                    queue.append((node.right, 2 * index + 1))
            max_width = max(max_width, level_end - level_start + 1)

        return max_width
