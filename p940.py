class Solution:
    def distinctSubseqII(self, s: str) -> int:
        MOD = 10**9 + 7

        dp = [0] * 26

        for c in s:
            i = ord(c) - ord('a')
            total = sum(dp) + 1
            dp[i] = total % MOD

        return sum(dp) % MOD