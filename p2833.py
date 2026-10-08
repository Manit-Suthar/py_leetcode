class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        c_pos = 0
        blank = 0
        for direction in moves:
            if direction == 'L':
                c_pos -= 1
            elif direction == 'R':
                c_pos += 1
            else:
                blank += 1    
        return abs(c_pos) + blank
    
ex = Solution()
str = "LLRRR___"
print(ex.furthestDistanceFromOrigin(str))
