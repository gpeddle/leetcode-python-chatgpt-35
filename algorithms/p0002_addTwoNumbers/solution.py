# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1, l2):
        carry = 0  # Initialize carry to 0
        dummy_head = ListNode()  # Create a dummy head node for the result
        current = dummy_head  # Initialize the current node to the dummy head

        while l1 or l2 or carry:
            # Get values from the two lists (if available) and add carry
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            # Calculate the sum and carry for the current digit
            total = val1 + val2 + carry
            carry = total // 10
            current_digit = total % 10

            # Create a new node for the result and move the current node
            current.next = ListNode(current_digit)
            current = current.next

            # Move to the next nodes in the input lists (if available)
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummy_head.next  # Return the result linked list starting from the next node of the dummy head
