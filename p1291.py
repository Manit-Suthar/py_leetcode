#sequential digits
from typing import List

class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        s1 = len(str(low))
        s2 = len(str(high))
        digitStr= "123456789" # as constrain is high could be as large as 10^9
        digitlist = []
        for length in range (s1,s2+1):
            for start in range (10-length):
                digit = int(digitStr[start:start+length])
                if(low<=digit<=high):
                    digitlist.append(digit)

        return digitlist
    
print(Solution().sequentialDigits(100,1000))

#expected 123,234,345,456,567,678,789