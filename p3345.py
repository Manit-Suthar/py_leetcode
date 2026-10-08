class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        product = 1
        while product%t != 0:
            temp = n 

            while temp > 0:
                product *= temp%10
                temp = temp//10

            if product%t == 0:
                return n 
            else:
                n += 1 
                product = 1

        return n

print(Solution().smallestNumber(1,6))