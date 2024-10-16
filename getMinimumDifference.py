class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        stack = []
        current = root
        prev = None
        minDif = float('inf')

        # In-order traversal
        while stack or current:
            # Reach the leftmost node of the current node
            while current:
                stack.append(current)
                current = current.left

            # Current node is the leftmost node
            current = stack.pop()

            # If there's a previous node, compare the difference
            if prev is not None:
                minDif = min(minDif, current.val - prev.val)

            # Update the previous node to the current one
            prev = current

            # Move to the right subtree
            current = current.right

        return minDif
