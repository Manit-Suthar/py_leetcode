class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
       i = 0 
       nums1 = nums[i]
       nums2 = target - nums1
       while nums2 not in nums[i+1:]:
           i+=1
           nums1 = nums[i]
           nums2 = target - nums1
           print(nums1,nums2)
           print(nums[i:].index(nums2))

       return i,nums[i+1:].index(nums2)+i+1
nums = [-1,-2,-3,-4,-5]
target = -8
print(Solution().twoSum(nums,target))