class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        my_set = set()
        for element in nums :
            if element in my_set : 
                return True
            else :
                my_set.add(element)
        else : 
            return False