class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# o(n) time and space
def branchSums(root):
    sums=[]
    calculateBranchSums(root, 0, sums)
    return sums





def calculateBranchSums(node,runningSum,sums):
    if node is None:
        return
    newRunningSum=runningSum + node.value
    if node.left is None and node.right is None :
        sums.append(newRunningSum)
        return
    
    calculateBranchSums(node.left, newRunningSum, sums)    
    calculateBranchSums(node.right, newRunningSum, sums)    
   
    
    
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

tree = create_bst()

sumArray=branchSums(tree)
