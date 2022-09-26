class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        bool_list = [False] * n
        ans = []
        for element in nums :
            bool_list[element-1] = True
        for i in range(len(bool_list)) : 
            if bool_list[i] == False :
                ans.append(i + 1)
        return ans