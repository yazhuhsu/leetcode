class Solution:
    def climbStairs(self, n: int) -> int:
        steps = 0
        
        for double_step in range(0, n):
            #step = tuple()
            step = 0
            
            single_step = n - 2 * double_step
            if single_step >= 0:
                #for single in range(single_step):
                #    step += (1,)
                #for double in range(i):
                #    step += (2,)
                step = single_step + double_step
                
                denominator = 1
                molecular = 1
                
                for i in range(1, single_step + 1):
                    denominator = denominator * (step + 1 - i)
                    molecular = molecular * i
                    
                steps = steps + int(denominator / molecular)

        return steps
            