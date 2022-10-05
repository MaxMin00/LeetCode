class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        pair_sum = []
        
        size = len(nums)
        k = size//2
        
        for i in range(k) :
            #gaussian addition
            pair_sum.append(nums[i] + nums[size - 1 - i])
        return max(pair_sum)