class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        outputs = []
        for i in range(rowIndex+1):
            output = []
            for j in range(i+1):
                if j in [0, i]:
                    output.append(1)
                    continue

                output.append(outputs[i-1][j-1]+outputs[i-1][j])

            outputs.append(output)

        return outputs[rowIndex]