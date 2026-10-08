#max product of 2 digits
class Solution:
    def maxProduct(self, n: int) -> int:
        digits = []
        while n:
            digits.append(n % 10)
            n //= 10
        first = second = float('-inf')
        for d in digits:
            if d > first:
                second = first
                first = d
            elif d > second:
                second = d        
        
        return first*second
    
print(Solution().maxProduct(364))