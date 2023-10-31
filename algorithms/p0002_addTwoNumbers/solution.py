# addTwoNumbers

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self) -> str:
        return f"{self.val} -> {self.next}"

    def __eq__(self, other):
        if not isinstance(other, ListNode):
            return False

        while self and other:
            if self.val != other.val:
                return False
            self = self.next
            other = other.next

        # If both linked lists are exhausted, they are equal
        return self is None and other is None


class Solution:
    def addTwoNumbers(self, l1, l2):
        carry = 0
        dummy_head = ListNode(0)
        current = dummy_head

        while l1 or l2:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            _sum = x + y + carry

            carry = _sum // 10
            current.next = ListNode(_sum % 10)

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

            current = current.next

        if carry > 0:
            current.next = ListNode(carry)

        return dummy_head.next
