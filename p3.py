#longest substring without repeating characters
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()
        left = 0
        max_len = 0

        for right in range(len(s)):
            # Step 1: if s[right] is already in the window, shrink from the left
            # until the duplicate is removed
            while s[right] in window:
                window.remove(s[left])
                left += 1

            # Step 2: now it's safe to add s[right]
            window.add(s[right])

            # Step 3: update the answer using current valid window size
            max_len = max(max_len, right - left + 1)

        return max_len
        
print(Solution().lengthOfLongestSubstring("abcabcbb"))