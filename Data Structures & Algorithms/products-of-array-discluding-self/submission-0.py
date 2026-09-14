class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = 1
        ans = []
        for i in nums:
            ans.append(prefix)
            prefix *= i
   
        
        suffix = nums[-1]

        for j in range(len(nums)-2,-1,-1):
            ans[j] *= suffix
            suffix *= nums[j]

        return ans