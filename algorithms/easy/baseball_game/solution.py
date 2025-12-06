class Solution:
    def calPoints(self, operations: list) -> int:
        scores = []
        for idx, operation in enumerate(operations):
            if operation == '+':
                scores.append(scores[len(scores)-2]+scores[len(scores)-1])
            elif operation == 'C':
                scores.pop()
            elif operation == 'D':
                scores.append(scores[len(scores)-1]*2)
            else:
                scores.append(int(operation))

        total_score = 0
        for _, score in enumerate(scores):
            total_score += score

        return total_score 

solution = Solution()
print(solution.calPoints(["5","2","C","D","+"])==30)
print(solution.calPoints(["5","-2","4","C","D","9","+","+"])==27)
print(solution.calPoints(["1","C"])==0)