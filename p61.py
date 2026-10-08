from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        # Step 1: find length
        length = 1
        temp = head
        while temp.next:
            temp = temp.next
            length += 1

        # Step 2: make circular
        temp.next = head

        # Step 3: reduce k
        k = k % length

        # Step 4: find new tail
        steps = length - k
        new_tail = head
        for _ in range(steps - 1):
            new_tail = new_tail.next

        # Step 5: break circle
        new_head = new_tail.next
        new_tail.next = None

        return new_head
    
# Example usage:
# Create a linked list 1 -> 2 -> 3 -> 4 -> 5
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
k = 2