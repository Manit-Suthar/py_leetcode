#GCD of Odd and Even Sums
# The sum of first n odd numbers is n*n
# The sum of first n even numers is n*(n+1)
# Gcd of n and n+1 is 1
# GCD of N*N and N*(N+1) is N * GCD of (N,N+1) = N

class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        return n
        
obj = Solution()        
print(obj.gcdOfOddEvenSums(5))