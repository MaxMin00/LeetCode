class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = []
        memo = [False] * (len(s) + 1)
        memo[0] = True
       
        for i in range(len(s)) :
            for w in range(i, len(s)) :
                if memo[i] and s[i : w + 1] in wordDict :
                    memo[w+1] = True                
        return memo[-1]
            