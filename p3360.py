class Solution:
    def canAliceWin(self, n: int) -> bool:
        current = 10
        i = 1
        print(n , current)
        while n >= current :
            n = n-current
            current -= 1
            i += 1         
        return i%2==0
    
print(Solution().canAliceWin(12))
print(Solution().canAliceWin(1))