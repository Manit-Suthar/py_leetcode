class Solution:

  def minimumDeletions(self, nums: list[int]) -> int:
    n = len(nums)
    if n <= 2:
      return n

    # Single pass to find both min and max indices
    min_i, max_i = 0, 0
    for i in range(1, n):
      if nums[i] < nums[min_i]:
        min_i = i
      if nums[i] > nums[max_i]:
        max_i = i

    # Ensure min_i is the smaller index for easier math
    if min_i > max_i:
      min_i, max_i = max_i, min_i

    # Calculate the three deletion strategies
    del_front = max_i + 1
    del_back = n - min_i
    del_both = (min_i + 1) + (n - max_i)

    return min(del_front, del_back, del_both)
