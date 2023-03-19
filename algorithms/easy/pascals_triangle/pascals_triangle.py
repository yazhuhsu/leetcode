class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        outputs = []

        for i in range(numRows):
            output = []
            for j in range(i+1):
                if j == 0 or j == i:
                    output.append(1)
                    continue

                output.append(outputs[i-1][j-1]+outputs[i-1][j])

            outputs.append(output)

        return outputs