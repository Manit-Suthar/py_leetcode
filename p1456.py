#max numbers pf vowels in substring 
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a','e','i','o','u'}
        count = 0 
        for i in range(k):
            if(s[i] in vowels):
                count+=1
        maxvowels = count
        for right in range(k,len(s)):
            if(s[right-k] in vowels):
                count-=1
            if(s[right] in vowels):
                count+=1
                maxvowels=max(maxvowels,count)
        return maxvowels
    
print(Solution().maxVowels("abciiidef",3))