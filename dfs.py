class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []



def create_general_tree():
    root = TreeNode('A')
    child1 = TreeNode('B')
    child2 = TreeNode('C')
    child3 = TreeNode('D')
    child4 = TreeNode('E')
    child5 = TreeNode('F')
    child6 = TreeNode('G')
    child7 = TreeNode('H')
    child8 = TreeNode('I')
    child9 = TreeNode('J')
    child10 = TreeNode('K')


    root.children.append(child1)
    root.children.append(child2)
    root.children.append(child3)
    child1.children.append(child4)
    child1.children.append(child5)
    child5.children.append(child8)
    child5.children.append(child9)
    child3.children.append(child6)
    child3.children.append(child7)
    child6.children.append(child10)
    
    
    
    return root

#o(v+e) time, o(v) space

def dfs(node,array):
    if node is None:
        return 
    
    print(node.value)  # Visit the node
    array.append(node.value)
    
    for child in node.children:
        dfs(child,array)  # Visit the children recursively

array=[]
tree = create_general_tree()
dfs(tree,array)
