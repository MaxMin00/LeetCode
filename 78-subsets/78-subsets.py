class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        #initialsing blank list
        output = []
        subset = []
        size = len(nums)
        
        def backTrack(self, index : int, subset : List[int]) :
            #reach each node
            output.append(subset.copy())

            #iterate through nodes
            for i in range(index, size) :
                backTrack(self, i+1, subset + [nums[i]])
        
        backTrack(self, 0, subset)
        
        return output
        