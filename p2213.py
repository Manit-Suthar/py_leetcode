
from typing import List


class Node:
    def __init__(self, l=0, r=0):
        self.l = l
        self.r = r
        self.lmx = 1
        self.rmx = 1
        self.mx = 1


class SegmentTree:
    def __init__(self, s):
        self.s = list(s)
        self.n = len(s)
        self.tree = [None] * (4 * self.n)
        self.build(1, 0, self.n - 1)

    def build(self, node, l, r):
        self.tree[node] = Node(l, r)

        if l == r:
            return

        mid = (l + r) // 2

        self.build(node * 2, l, mid)
        self.build(node * 2 + 1, mid + 1, r)

        self.push_up(node)

    def push_up(self, node):
        left = self.tree[node * 2]
        right = self.tree[node * 2 + 1]
        cur = self.tree[node]

        cur.lmx = left.lmx
        cur.rmx = right.rmx
        cur.mx = max(left.mx, right.mx)

        left_len = left.r - left.l + 1
        right_len = right.r - right.l + 1

        if self.s[left.r] == self.s[right.l]:

            # Prefix can extend into right segment
            if left.lmx == left_len:
                cur.lmx += right.lmx

            # Suffix can extend into left segment
            if right.rmx == right_len:
                cur.rmx += left.rmx

            # Longest sequence crossing the middle
            cur.mx = max(cur.mx, left.rmx + right.lmx)

    def update(self, node, index, ch):
        cur = self.tree[node]

        if cur.l == cur.r:
            self.s[index] = ch
            return

        mid = (cur.l + cur.r) // 2

        if index <= mid:
            self.update(node * 2, index, ch)
        else:
            self.update(node * 2 + 1, index, ch)

        self.push_up(node)


class Solution:
    def longestRepeating(
        self,
        s: str,
        queryCharacters: str,
        queryIndices: List[int]
    ) -> List[int]:

        tree = SegmentTree(s)

        ans = []

        for index, ch in zip(queryIndices, queryCharacters):
            tree.update(1, index, ch)
            ans.append(tree.tree[1].mx)

        return ans