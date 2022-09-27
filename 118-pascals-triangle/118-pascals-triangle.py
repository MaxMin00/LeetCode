class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        output = []
        
        for i in range(numRows):
            row = []
            for j in range(0,i + 1):
                #
                if i == j or j==0:
                    row.append(1)
                else:
                    row.append(output[i-1][j-1]+output[i-1][j])
                    
            output.append(row)
            
        return output