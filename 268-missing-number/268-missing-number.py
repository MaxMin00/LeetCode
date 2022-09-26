class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        myList = list(range(n+1))
        print(myList)
        for element in myList :
            print('.')
            if not element in nums :
                return element