class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None




def create_bst():
    root = BST(10)
    root.left = BST(5)
    root.right = BST(15)
    root.left.left = BST(2)
    root.left.right = BST(5)
    root.left.left.left = BST(1)
    root.right.left = BST(13)
    root.right.right = BST(22)
    root.right.left.right = BST(14)
    return root


# o(log(n)) both space and time on avg
def findClosestValueInBst(tree,target):

    return findClosestValueInBstHelper(tree,target,float("inf"))

    
    
def findClosestValueInBstHelper(tree,target,closest):
    if tree is None:
        return closest
    if abs(target-closest)>abs(target-tree.value):
        closest=tree.value
    if tree.value>target:
        return findClosestValueInBstHelper(tree.left, target, closest)
    if tree.value<target:
        return findClosestValueInBstHelper(tree.right, target, closest)
    else: return closest
    
    
    
tree = create_bst()
target = 12    
closest_value=findClosestValueInBst(tree, target)

