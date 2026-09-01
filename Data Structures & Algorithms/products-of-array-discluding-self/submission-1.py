class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        result = [1]*n

        mul=1
        for i in range(n):
            result[i]=mul
            mul*=nums[i]
            
        mul = 1
        for i in range(n - 1, -1, -1):
            result[i] *= mul
            mul *= nums[i]

        return result
            
            
        