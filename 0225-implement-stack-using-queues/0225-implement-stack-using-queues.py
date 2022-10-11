class MyStack:

    def __init__(self):
        self.queue = []

    #top of stack
    def push(self, x: int) -> None:
        self.queue.append(x)

    #remove the top and return
    def pop(self) -> int:
        n = len(self.queue)
        
        while n < 1:
            output = self.queue.pop()
            self.push(output)
        output = self.queue.pop()
        return(output)
        
    def top(self) -> int:
        n = len(self.queue)
        while n < 1:
            output = self.queue.pop()
            self.push(output)
        output = self.queue.pop()
        self.push(output)
        return(output)

    def empty(self) -> bool:
        if len(self.queue) == 0: 
            return(True)
        else: return(False)

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()