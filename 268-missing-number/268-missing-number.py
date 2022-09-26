class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        myList = list(range(n+1))
        for element in myList :
            if not element in nums :
                return element