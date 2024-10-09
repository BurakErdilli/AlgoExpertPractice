class MinMaxStack:
    def __init__(self):
        self.minMaxStack = []
        self.stack = []

    def peek(self):
        return self.stack[len(self.stack) - 1]

    def pop(self):
        self.minMaxStack.pop()
        return self.stack.pop()

    def push(self, number):
        newMinMax = {"min": number, "max": number}
        if len(self.minMaxStack) > 0:
            lastMinMax = self.minMaxStack[len(self.minMaxStack) - 1]
            newMinMax["min"] = min(lastMinMax["min"], number)
            newMinMax["max"] = max(lastMinMax["max"], number)
        self.minMaxStack.append(newMinMax)
        self.stack.append(number)

    def getMin(self):
        return self.minMaxStack[len(self.minMaxStack) - 1]["min"]

    def getMax(self):
        return self.minMaxStack[len(self.minMaxStack) - 1]["max"]


# Create an instance of MinMaxStack
stack = MinMaxStack()

# Push some numbers onto the stack
stack.push(5)
stack.push(1)
stack.push(7)
stack.push(3)
stack.push(9)

# Print current stack
print("Stack after pushes:", stack.stack)  # Expected: [5, 1, 7, 3, 9]

# Print current min and max
print("Current Min:", stack.getMin())  # Expected: 1
print("Current Max:", stack.getMax())  # Expected: 9

# Pop a number from the stack
print("Popped value:", stack.pop())  # Expected: 9

# Print stack after popping
print("Stack after pop:", stack.stack)  # Expected: [5, 1, 7, 3]

# Print current min and max
print("Current Min:", stack.getMin())  # Expected: 1
print("Current Max:", stack.getMax())  # Expected: 7

# Push more numbers onto the stack
stack.push(4)
stack.push(0)

# Print stack after more pushes
print("Stack after more pushes:", stack.stack)  # Expected: [5, 1, 7, 3, 4, 0]

# Print current min and max
print("Current Min:", stack.getMin())  # Expected: 0
print("Current Max:", stack.getMax())  # Expected: 7
