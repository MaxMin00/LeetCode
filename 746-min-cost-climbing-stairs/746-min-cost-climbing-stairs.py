class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        ans = []
        ans.append(0)
        i = len(cost)
        #base case
        if  i < 2 :
            return 0
        else :
            for j in range(1, i) :
                ans.append(min(ans[j-1] + cost[j], ans[j-2] + cost[j-1]))
            return ans[-1]