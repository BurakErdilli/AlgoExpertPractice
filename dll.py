class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def setHead(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.insertBefore(self.head, node)

    def setTail(self, node):
        if self.tail is None:
            self.setHead(node)
        else:
            self.insertAfter(self.tail, node)

    def insertBefore(self, node, nodeToInsert):
        if nodeToInsert == self.head and nodeToInsert == self.tail:
            return
        self.remove(nodeToInsert)
        nodeToInsert.prev = node.prev
        nodeToInsert.next = node
        if node.prev is None:
            self.head = nodeToInsert
        else:
            node.prev.next = nodeToInsert
        node.prev = nodeToInsert

    def insertAfter(self, node, nodeToInsert):
        if nodeToInsert == self.head and nodeToInsert == self.tail:
            return
        self.remove(nodeToInsert)
        nodeToInsert.prev = node
        nodeToInsert.next = node.next
        if node.next is None:
            self.tail = nodeToInsert
        else:
            node.next.prev = nodeToInsert
        node.next = nodeToInsert

    def insertAtPosition(self, position, nodeToInsert):
        if position == 1:
            self.setHead(nodeToInsert)
            return
        current = self.head
        currentPosition = 1
        while current is not None and currentPosition != position:
            current = current.next
            currentPosition += 1
        if current is not None:
            self.insertBefore(current, nodeToInsert)
        else:
            self.setTail(nodeToInsert)

    def removeNodesWithValue(self, value):
        current = self.head
        while current is not None:
            nodeToRemove = current
            current = current.next
            if nodeToRemove.value == value:
                self.remove(nodeToRemove)

    def remove(self, node):
        if node == self.head:
            self.head = self.head.next
        if node == self.tail:
            self.tail = self.tail.prev
        self.removeNodeBindings(node)

    def removeNodeBindings(self, node):
        if node.prev is not None:
            node.prev.next = node.next
        if node.next is not None:
            node.next.prev = node.prev
        node.prev = None
        node.next = None

    def containsNodeWithValue(self, value):
        current = self.head
        while current is not None:
            if current.value == value:
                return True
            current = current.next
        return False

    # Helper method to visualize the list
    def printList(self):
        current = self.head
        values = []
        while current is not None:
            values.append(current.value)
            current = current.next
        print("Doubly Linked List:", values)


# Create 12 nodes
nodes = [Node(i) for i in range(1, 13)]

# Initialize the doubly linked list
dll = DoublyLinkedList()

# Test setting head and tail
dll.setHead(nodes[0])   # Set node 1 as head
dll.setTail(nodes[11])  # Set node 12 as tail
dll.printList()         # Should print: [1, 12]

# Test insertAfter
dll.insertAfter(nodes[0], nodes[1])  # Insert node 2 after node 1
dll.printList()                      # Should print: [1, 2, 12]

# Test insertBefore
dll.insertBefore(nodes[1], nodes[2])  # Insert node 3 before node 2
dll.printList()                       # Should print: [1, 3, 2, 12]

# Test insertAtPosition
dll.insertAtPosition(3, nodes[3])  # Insert node 4 at position 3
dll.printList()                    # Should print: [1, 3, 4, 2, 12]

# Test inserting more nodes
dll.insertAtPosition(5, nodes[4])  # Insert node 5 at position 5
dll.setTail(nodes[5])              # Set node 6 as new tail
dll.printList()                    # Should print: [1, 3, 4, 2, 5, 6]

# Insert the remaining nodes
dll.insertAfter(nodes[5], nodes[6])  # Insert node 7 after node 6
dll.insertAfter(nodes[6], nodes[7])  # Insert node 8 after node 7
dll.insertAfter(nodes[7], nodes[8])  # Insert node 9 after node 8
dll.insertAfter(nodes[8], nodes[9])  # Insert node 10 after node 9
dll.insertAfter(nodes[9], nodes[10]) # Insert node 11 after node 10
dll.printList()                      # Should print: [1, 3, 4, 2, 5, 6, 7, 8, 9, 10, 11, 12]

# Test remove
dll.remove(nodes[4])  # Remove node 5
dll.printList()       # Should print: [1, 3, 4, 2, 6, 7, 8, 9, 10, 11, 12]

# Test removeNodesWithValue
dll.removeNodesWithValue(2)  # Remove all nodes with value 2
dll.printList()              # Should print: [1, 3, 4, 6, 7, 8, 9, 10, 11, 12]

# Test containsNodeWithValue
print(dll.containsNodeWithValue(10))  # Should return True
print(dll.containsNodeWithValue(5))   # Should return False
