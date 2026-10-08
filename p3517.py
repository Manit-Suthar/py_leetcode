#smallest lexicographical pelindrom 
class Solution:
    def smallestPalindrome(self, s: str) -> str:
        arr = [0] * 26

        for c in s:
            arr[ord(c) - ord('a')] += 1

        left = []
        middle = ""

        for i in range(26):
            left.append(chr(ord('a') + i) * (arr[i] // 2))

            if arr[i] % 2 == 1:
                middle = chr(ord('a') + i)

        left = "".join(left)

        return left + middle + left[::-1]