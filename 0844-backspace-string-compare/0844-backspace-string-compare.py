class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        ss, ts = [], []
        
        for i in s:
            if ss and i == '#':
                ss.pop()
            elif ss == [] and i == '#': 
                continue         
            else:
                ss.append(i)
                
                
        for j in t:
            if ts and j == '#':
                ts.pop()
            elif ts == [] and j == '#': 
                continue
            else:
                ts.append(j)
        
        print(ss, ts)
        
        if ss == ts :
            return True