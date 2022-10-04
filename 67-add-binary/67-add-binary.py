class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a_int = 0
        b_int = 0
        
        for i in range(len(a) - 1, -1, -1) :
            a_int += 2**i * int(a[len(a) - 1 - i])
            
        for i in range(len(b)-1, -1, -1) :
            b_int += 2**i * int(b[len(b) - 1 - i])
        
        num = a_int + b_int 
        remainder = 0
        stack = ""
        
        while (num > 0) :
            remainder = num % 2
            num = num // 2
            stack += str(remainder)
        
        if(len(stack) == 0) :
            stack = "0"
            
        return stack[::-1]