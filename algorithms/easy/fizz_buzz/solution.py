class Solution:
    def fizzBuzz(self, n: int) -> []:
        output = []
        for i in range (1, n+1):
            s = ''
            if i % 3 == 0:
                s += 'Fizz'
            if i % 5 == 0:
                s += 'Buzz'

            if s == '':
                s += str(i)
        
            output.append(s)

        return output 
        
cases = {
    3:  ['1', '2', 'Fizz'],
	5:  ['1', '2', 'Fizz', '4', 'Buzz'],
	15: ['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz', 'Buzz', '11', 'Fizz', '13', '14', 'FizzBuzz'],
}

solution = Solution()
for k, v in cases.items():
    answers = solution.fizzBuzz(k)
    for i in range(len(v)):
        if v[i] != answers[i]:
            print(f'n={k} Wrong!')
            print(f'output:{v}, answer:{answers}')
            break
    
    print(f'n={k} Correct!')