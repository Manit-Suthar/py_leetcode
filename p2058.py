# Definition for singly-linked list.
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        first = -1
        prev_critical = -1

        min_dist = float('inf')
        index = 1

        prev = head
        curr = head.next

        while curr and curr.next:
            if (curr.val > prev.val and curr.val > curr.next.val) or \
               (curr.val < prev.val and curr.val < curr.next.val):

                if first == -1:
                    first = index
                else:
                    min_dist = min(min_dist, index - prev_critical)

                prev_critical = index

            prev = curr
            curr = curr.next
            index += 1

        if first == -1 or first == prev_critical:
            return [-1, -1]

        max_dist = prev_critical - first

        return [min_dist, max_dist]

l1 = ListNode(5)
l2 = ListNode(3)
l3 = ListNode(1)
l4 = ListNode(2)
l5 = ListNode(5)
l6 = ListNode(1)
l7 = ListNode(2)
l1.next = l2
l2.next = l3
l3.next = l4
l4.next = l5
l5.next = l6
l6.next = l7
print(Solution().nodesBetweenCriticalPoints(l1))