class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        currentNode = self
        while True:
            if value < currentNode.value:
                if currentNode.left is None:
                    currentNode.left = BST(value)
                    break
                currentNode = currentNode.left

            elif value >= currentNode.value:
                if currentNode.right is None:
                    currentNode.right = BST(value)
                    break
                currentNode = currentNode.right
        return self

    def contains(self, value):
        currentNode = self
        while currentNode is not None:
            if currentNode.value == value:
                return True
            elif currentNode.value > value:
                currentNode = currentNode.left
            else:
                currentNode = currentNode.right

        return False

    # def remove(self, value, parentNode=None):
    #     currentNode = self
    #     while currentNode is not None:
    #         if value < currentNode.value:
    #             parentNode=currentNode
    #             currentNode=currentNode.left
    #         elif value > currentNode.value:
    #             parentNode=currentNode
    #             currentNode=currentNode.right
    #         else:
    #             if currentNode.left is not None and currentNode.right is not None:
    #                 currentNode.value = currentNode.right.ge
