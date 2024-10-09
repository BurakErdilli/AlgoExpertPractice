class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def setHead(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head = node

    def setTail(self, node):
        if self.tail is None:
            self.setHead(node)
        else:
            self.tail.next = node
            self.tail = node

    def insertAfter(self, node, nodeToInsert):
        if nodeToInsert == self.head and nodeToInsert == self.tail:
            return
        nodeToInsert.next = node.next
        node.next = nodeToInsert
        if nodeToInsert.next is None:
            self.tail = nodeToInsert

    def insertAtPosition(self, position, nodeToInsert):
        if position == 1:
            self.setHead(nodeToInsert)
            return
        current = self.head
        currentPosition = 1
        while current is not None and currentPosition != position - 1:
            current = current.next
            currentPosition += 1
        if current is not None:
            self.insertAfter(current, nodeToInsert)

    def remove(self, node):
        if self.head is None:
            return
        if self.head == node:
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            return

        current = self.head
        while current.next is not None and current.next != node:
            current = current.next

        if current.next == node:
            current.next = node.next
            if current.next is None:
                self.tail = current

    def removeNodesWithValue(self, value):
        current = self.head
        while current is not None and current.value == value:
            self.head = current.next
            current = self.head

        prev = None
        while current is not None:
            if current.value == value:
                prev.next = current.next
                if current == self.tail:
                    self.tail = prev
            else:
                prev = current
            current = current.next

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
        print("Singly Linked List:", values)

    def removeNthNodeFromEnd(self, n, size):
        i = self.head
        j = self.head
        if n > size:
            print('index is bigger than the ssl size')
            return -1
        for node in range(n-1):
            j = j.next
        while j.next != None:
            i = i.next
            j = j.next

        return i.value

    def findListSize(self):
        if self.head is None:
            return 0
        currentNode = self.head
        size = 1
        while currentNode.next != None:
            size += 1
            currentNode = currentNode.next
        return size


# Create 12 nodes
nodes = [Node(i) for i in range(1, 13)]

# Initialize the singly linked list
sll = LinkedList()

# Test setting head and tail
sll.setHead(nodes[0])   # Set node 1 as head
sll.setTail(nodes[11])  # Set node 12 as tail
sll.printList()         # Should print: [1, 12]

# Test insertAfter
sll.insertAfter(nodes[0], nodes[1])  # Insert node 2 after node 1
sll.printList()                      # Should print: [1, 2, 12]

# Test insertAtPosition
sll.insertAtPosition(3, nodes[2])  # Insert node 3 at position 3
sll.printList()                    # Should print: [1, 2, 3, 12]

# Test inserting more nodes
sll.insertAtPosition(4, nodes[3])  # Insert node 4 at position 4
sll.setTail(nodes[4])              # Set node 5 as new tail
sll.printList()                    # Should print: [1, 2, 3, 4, 5]

# Insert the remaining nodes
sll.insertAfter(nodes[4], nodes[5])  # Insert node 6 after node 5
sll.insertAfter(nodes[5], nodes[6])  # Insert node 7 after node 6
sll.insertAfter(nodes[6], nodes[7])  # Insert node 8 after node 7
sll.insertAfter(nodes[7], nodes[8])  # Insert node 9 after node 8
sll.insertAfter(nodes[8], nodes[9])  # Insert node 10 after node 9
sll.insertAfter(nodes[9], nodes[10])  # Insert node 11 after node 10
# Should print: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
sll.printList()

# Test remove
sll.remove(nodes[3])  # Remove node 4
sll.printList()       # Should print: [1, 2, 3, 5, 6, 7, 8, 9, 10, 11, 12]

# Test removeNodesWithValue
sll.removeNodesWithValue(2)  # Remove all nodes with value 2
sll.printList()              # Should print: [1, 3, 5, 6, 7, 8, 9, 10, 11, 12]

# Test containsNodeWithValue
print(sll.containsNodeWithValue(10))  # Should return True
print(sll.containsNodeWithValue(4))   # Should return False
index = 9
size = sll.findListSize()
a = sll.removeNthNodeFromEnd(index, size)
print(a)
