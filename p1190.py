class Solution:
    def reverseParentheses(self, s: str) -> str:
        n = len(s)
        pair = [0] * n
        openings = []

        for i, ch in enumerate(s):
            if ch == "(":
                openings.append(i)
            elif ch == ")":
                j = openings.pop()
                pair[i] = j
                pair[j] = i

        answer = []
        i = 0
        direction = 1

        while 0 <= i < n:
            if s[i] == "(" or s[i] == ")":
                i = pair[i]
                direction = -direction
            else:
                answer.append(s[i])

            i += direction

        return "".join(answer)