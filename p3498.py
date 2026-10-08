class Solution:
    def reverseDegree(self, s: str) -> int:
        sum = 0 
        for i,ch in enumerate(s):
            
            sum+=(i+1)*abs((ord(ch)-97)-26)
        return sum 
print(Solution().reverseDegree("abc"))

# class Solution:
#     def reverseDegree(self, s: str) -> int:

#         ans, idx = 0, 1
#         for ch in s:
#             ans+= (123 - ord(ch)) * idx
#             idx+= 1

#         return ans    