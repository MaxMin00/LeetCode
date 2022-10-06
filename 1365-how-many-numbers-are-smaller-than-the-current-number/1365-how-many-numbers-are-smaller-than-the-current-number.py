class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_num = sorted(nums)
        output = []
        
        for i in range(len(nums)) :
            counter = 0
            for j in range(sorted_num.index(nums[i])) :
                if(sorted_num[j] < nums[i]) :
                    counter += 1
                else :
                    break;
            output.append(counter)
            
        return output