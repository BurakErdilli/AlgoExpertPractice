def validateBts(tree):
    if tree is None:
        return True
    if tree.value < tree.left.value or tree.value > tree.right.value:
        return False
    leftIsValid = validateBts(tree.left)
    rightIsValid = validateBts(tree.right)

    return leftIsValid and rightIsValid


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def validateBst(tree, minValue=None, maxValue=None):
    if tree is None:
        return True
    if (minValue is not None and tree.value <= minValue) or (maxValue is not None and tree.value >= maxValue):
        return False
    leftIsValid = validateBst(tree.left, minValue, tree.value)
    rightIsValid = validateBst(tree.right, tree.value, maxValue)

    return leftIsValid and rightIsValid


# Example to test
root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)
root.left.left = TreeNode(2)
root.left.right = TreeNode(7)
root.right.left = TreeNode(12)
root.right.right = TreeNode(20)

# Should return True because this is a valid BST
print("Is valid BST:", validateBst(root))

# Now, let's break the BST property
root.right.left.value = 17

# Should return False because 17 is in the wrong place
print("Is valid BST after modification:", validateBst(root))
