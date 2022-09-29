class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # O(log n) : binary search
        size = len(nums)
        
        def recur(low, high, nums) :
            # base case found or no value found
            if low > high :
                return low
            idx = (low + high) // 2
            
            if target == nums[idx] :
                return idx
            
            #check if there are idx has to go right
            elif (nums[idx] < target) : 
                return recur(idx + 1,high, nums)
            
            #check if there are idx has to go left
            elif (nums[idx] > target) :
                return recur(low, idx - 1, nums)
        
        return recur(0, size -1, nums)
            
        