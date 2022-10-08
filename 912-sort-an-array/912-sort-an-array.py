class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        #nlogn : heapsort, mergesort, quicksort
        
        heapq.heapify(nums)
        sort = []
        while nums:
            sort.append(heapq.heappop(nums))
        return sort