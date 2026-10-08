# min num of pushes to type word I
class Solution:
    def minimumPushes(self, word: str) -> int:
        l = len(word)
        if(l<=8):
            return l
        elif(l<=16):
            return 8+(2*(l-8))
        elif(l<=24):
            return 24+(3*(l-16))
        elif(l<=26):
            return 48+(4*(l-24))
        
print(Solution().minimumPushes("acolkxjbizfmhnrdq"))