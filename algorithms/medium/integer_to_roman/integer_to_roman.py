# Examples:   
# 1835: MDCCCXXXV
#   1835 // 1000 = 1 -> M (1835 - 1000*1 = 835)
#   835 // 500 = 1 -> D (835 - 500*1 = 335)
#   335 // 100 = 3 -> CCC (335 - 100*3 = 35)
#   35 // 10 = 3 -> XXX (35 - 10*3 = 5)
#   5 // 5 = 1 -> V

# 1994: MCMXCIV
#   1994 // 1000 = 1 -> M (1994 - 1000*1 = 994)
#   994 - 900 < 100 -> CM (994 - 900 = 94)
#   94 // 500 = 0
#   94 - 90 < 10 ->  XC (94 - 90 = 4)
#   4 // 5 = 0
#   4 - 4 < 1 -> IV

class Solution:
    def intToRoman(self, num: int) -> str:
        value_to_symbol = {
            1000: 'M',
            500:  'D',
            100:  'C',
            50:   'L',
            10:   'X',
            5:    'V',
            1:    'I'
        }

        output = ''
        origin = 100
        for idx, (v, s) in enumerate(value_to_symbol.items()):
            # handle value and symbol in dictionary:
            # example: num=300, v=100, s=C
            # 300//100=3 -> CCC
            count = num // v
            for c in range(count):
                output += s
                num -= v

            if v == 1:
                break

            # handle combinations
            # example: 990, v=1000, s=M, origin=100, origin_s=C
            # m = 1000-100 = 900
            # num - 900 >= 0, num - 900 < 100 -> CM
            m = v - origin
            if num - m >= 0 and num - m < origin:
                output += f'{value_to_symbol[origin]}{s}'
                num -= m

            # 1000, 500 -> 900, 400
            # 100, 50   -> 90, 40
            # 10, 5     -> 9, 4
            if idx % 2 == 1:
                origin = int(origin/10)

        return output