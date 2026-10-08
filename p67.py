class Solution:
    def addBinary(self, a: str, b: str) -> str:
        alen = len(a)
        blen = len(b)
        carry = 0
        temp = 0 
        sum = [] 
        while (alen > 0 or blen > 0 or carry > 0):
            temp = carry
            if(alen>0):
                temp += int(a[alen-1])
                alen-=1
            if(blen>0):
                temp += int(b[blen-1])
                blen-=1
            sum.append(str(temp%2))
            carry = temp//2
        return "".join(reversed(sum))
    
s = Solution()
a = '1010'
b = '1011'

print(s.addBinary(a, b))