
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode()
        current = dummy
        cf = 0
        while l1 or l2 or cf:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            val = v1+v2+cf

            cf = val//10
            val = val % 10

            current.next = ListNode(val)

            current = current.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next


obj = Solution()

l1 = ListNode(2)
l1.next = ListNode(3)

l2 = ListNode(1)
l2.next = ListNode(4)

result = obj.addTwoNumbers(l1, l2)

while result:
    print(result.val)
    result = result.next
