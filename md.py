from types import *

class MathDojo(object):
    def __init__(self):
        self.result = 0
    def add(self, *nums): 
        for num in nums:
            if type(num) is IntType:
                self.result += num
            else:
                for i in range(len(num)):
                    self.result += num[i] 
        return self
    def subtract(self, *nums):
        for num in nums:
            if type(num) is IntType:
                self.result -= num
            else:
                for i in range(len(num)):
                    self.result -= num[i] 
        return self
    def return_result(self):
        print self.result
        return self
    
#equation = MathDojo()
#equation.add(1,2,3,4).return_result().subtract(5,15).add(50).return_result()

equation = MathDojo()
equation.add([1],3,4).add([3, 5, 7, 8], (2, 4.3, 1.25)).subtract(2, [2,3], [1.1, 2.3]).return_result()
        

