class AncestralTree:
    def __init__(self, name):
        self.name = name
        self.ancestor = None


def getYoungestCommonAncestor(topAncestor, descendantOne, descendantTwo):
    depthOne = getDescendantDepth(descendantOne, topAncestor)
    depthTwo = getDescendantDepth(descendantTwo, topAncestor)
    if depthOne > depthTwo:
        descendantOne = getUpBy(descendantOne, depthOne-depthTwo)
    if depthTwo > depthOne:
        descendantTwo = getUpBy(descendantTwo, depthTwo-depthOne)
    while descendantOne != descendantTwo:
        descendantOne = descendantOne.ancestor
        descendantTwo = descendantTwo.ancestor
    return descendantOne.name


def getDescendantDepth(descendant, topAncestor):
    depth = 0
    while descendant != topAncestor:
        descendant = descendant.ancestor
        depth += 1
    return depth


def getUpBy(descendant, steps):
    for i in range(steps):
        descendant = descendant.ancestor

    return descendant


# Example of creating an ancestral tree:
# Example of creating an ancestral tree:
root = AncestralTree("A")
b = AncestralTree("B")
c = AncestralTree("C")
d = AncestralTree("D")
e = AncestralTree("E")
f = AncestralTree("F")
g = AncestralTree("G")
h = AncestralTree("H")
i = AncestralTree("I")  # New generation
j = AncestralTree("J")  # New generation

# Establishing the ancestor relationships
b.ancestor = root
c.ancestor = root
d.ancestor = b
e.ancestor = b
f.ancestor = c
g.ancestor = c
h.ancestor = d
i.ancestor = e  # New relationship
j.ancestor = g  # New relationship


# Example usage:
a = getYoungestCommonAncestor(root, f, j)
print(a)
