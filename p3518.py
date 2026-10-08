from typing import Counter


class Solution:
    MAX = 10**6 + 1

    def smallestPalindrome(self, s: str, k: int) -> str:
        count = Counter(s)

        half = [0] * 26
        mid = ""

        for c, v in count.items():
            idx = ord(c) - ord("a")
            half[idx] = v // 2
            if v & 1:
                mid = c

        if self._count(half) < k:
            return ""

        left = []

        for _ in range(sum(half)):
            for i in range(26):
                if half[i] == 0:
                    continue

                half[i] -= 1
                ways = self._count(half)

                if ways >= k:
                    left.append(chr(i + ord("a")))
                    break

                k -= ways
                half[i] += 1

        left = "".join(left)
        return left + mid + left[::-1]

    def _count(self, freq):
        total = sum(freq)
        ans = 1

        for f in freq:
            if f:
                ans *= self._nCk(total, f)
                if ans >= self.MAX:
                    return self.MAX
                total -= f

        return ans

    def _nCk(self, n, k):
        k = min(k, n - k)
        res = 1
        for i in range(1, k + 1):
            res = res * (n - i + 1) // i
            if res >= self.MAX:
                return self.MAX
        return res