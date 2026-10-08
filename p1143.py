#dp
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        # 2D ટેબલ (Grid) બનાવવું જેમાં શરૂઆતમાં બધા 0 હોય
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        # ટેબલને રો અને કોલમ વાઇઝ ભરવું (તમારા બે નિયમો મુજબ)
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    # નિયમ ૧: મેચ થાય તો ડાયગોનલ + ૧
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    # નિયમ ૨: મેચ ન થાય તો ઉપર અથવા ડાબી બાજુમાંથી જે મોટું હોય તે
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
                    
        # છેલ્લી સેલ (Bottom-Right) આપણો ફાઇનલ જવાબ આપશે
        return dp[m][n]
