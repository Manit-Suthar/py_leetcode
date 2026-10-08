class Solution:
    def longestValidParentheses(self, s: str) -> int:
        n = len(s)
        earliest = [-1] * (2 * n + 1)
        height = 0
        answer = 0

        earliest[n] = 0

        for position, ch in enumerate(s, 1):
            if ch == "(":
                height += 1
                earliest[height + n] = position
            else:
                earliest[height + n] = -1
                height -= 1

                index = height + n
                if earliest[index] == -1:
                    earliest[index] = position
                else:
                    answer = max(answer, position - earliest[index])

        return answer