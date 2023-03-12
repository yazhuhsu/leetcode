class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        alphabets = [a for a in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ']
        if columnNumber <= 26:
            return alphabets[columnNumber-1]
        else:
            title = ''
            mods = columnNumber % 26
            columns = []
            while columnNumber > 26 :
                if mods == 0:
                    columns.append(columnNumber//26-1)
                    columnNumber = columnNumber // 26 - 1
                else:
                    columns.append(columnNumber//26)
                    columnNumber = columnNumber // 26
            
            columns.reverse()

            for idx, num in enumerate(columns):
                if idx == 0:
                    c = num
                else:
                    c = num - (columns[idx-1]) * (26)
                title += alphabets[c-1]

            title += alphabets[mods-1]
            return title