class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        s1 = s.split()
        return " ".join(s1[:k])

print(Solution().truncateSentence('Hello How Are You Contestant',3))