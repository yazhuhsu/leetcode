class Solution:
    def myAtoi(self, s: str) -> int:
        symbol_idx, digit_idx = -1, -1
        symbols = []
        digits = []
        for idx, c in enumerate(s):
            if idx == 0 and \
             c not in ["-", "+", ' '] and \
             not c.isdigit():
                break
            
            if c.isdigit():
                if not digits:
                    digit_idx = idx
                digits.append(int(c))
            elif c in ["-", "+"]:
                if digits:
                    break
                if not symbols:
                    symbol_idx = idx
                symbols.append(c)
            elif c in ["."]:
                break
            elif c in [" "]:
                if digits:
                    break
                continue
            else:
                if digits:
                    break
                if idx + 1 < len(s) and s[idx+1].isdigit():
                    break

        if len(symbols) > 1:
            return 0
        print("symbol_idx: ", symbol_idx)
        print("digit_idx: ", digit_idx)
        if symbol_idx > digit_idx:
            return 0
        if symbol_idx != -1 and digit_idx != -1 and symbol_idx + 1 != digit_idx:
            return 0

        output = 0
        for idx, digit in enumerate(digits):
            print(digit)
            print((10**(len(digits)-(idx+1))))
            output += digit * (10**(len(digits)-(idx+1)))

        if symbols and symbols[0] == "-":
            output = -output

        min_value = -(2**31)
        max_value = 2**31-1
        if output < min_value:
            output = min_value
        if output > max_value:
            output = max_value

        return output