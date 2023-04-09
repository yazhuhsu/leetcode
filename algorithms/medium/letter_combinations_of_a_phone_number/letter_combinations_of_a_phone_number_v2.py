class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digits_to_letters = {
            2: ['a', 'b', 'c'],
            3: ['d', 'e', 'f'],
            4: ['g', 'h', 'i'],
            5: ['j', 'k', 'l'],
            6: ['m', 'n', 'o'],
            7: ['p', 'q', 'r', 's'],
            8: ['t', 'u', 'v'],
            9: ['w', 'x', 'y', 'z'],
        }

        if digits == "":
            return []
        if len(digits) == 1:
            return digits_to_letters[int(digits)]

        letters = []
        counts = []
        combinations = []
        for digit in digits:
            letters.append(digits_to_letters[int(digit)])
            counts.append(len(digits_to_letters[int(digit)]))

        for idx, letter in enumerate(letters):
            duplicates = 1
            for count in counts:
                duplicates *= count
            step = len(letter)

            cidx = 0
            didx = 0
            round_idx = 0
            for lidx, l in enumerate(letter):
                for duplicate in range(0, duplicates, step):
                    if idx == 0:
                        combinations.append(l)
                    elif idx < len(letters) - 1:
                        """
                        2345
                        ['a', 'b', 'c']
                        ['d', 'e', 'f']
                        ['g', 'h', 'i']
                        ['j', 'k', 'l']
                        -> d: 0, 1, 2, 3, 4, 5, 6, 7, 8, 
                              27, 28, 29, 30, 31, 32, 33, 34, 35,
                              54, 55, 56, 57, 58, 59, 60, 61, 62
                        -> e: 9, 10, 11, 12, 13, 14, 15, 16, 17,
                              36, 37, 38, 39, 40, 41, 42, 43, 44,
                              63, 64, 65, 66, 67, 68, 69, 70, 71
                        -> f: 18, 19, 20, 21, 22, 23, 24, 25, 26,
                              45, 46, 47, 48, 49, 50, 51, 52, 53,
                              72, 73, 74, 75, 76, 77, 78, 79, 80
                        -> g: 0, 1, 2, 
                              9, 10, 11,
                              18, 19, 20,
                              27, 28, 29,
                              36, 37, 38,
                              45, 46, 47,
                              54, 55, 56,
                              63, 64, 65,
                              72, 73, 74,
                        -> h: 3, 4, 5,
                              12, 13, 14,
                              21, 22, 23,
                              30, 31, 32,
                              39, 40, 41,
                              48, 49, 50,
                              57, 58, 59,
                              66, 67, 68,
                              75, 76, 77
                        -> i: 6, 7, 8,
                              15, 16, 17,
                              24, 25, 26,
                              33, 34, 35,
                              42, 43, 44,
                              51, 52, 53,
                              60, 61, 62,
                              69, 70, 71,
                              78, 79, 80
                        """
                        """
                        5678
                        ['j', 'k', 'l']
                        ['m', 'n', 'o']
                        ['p', 'q', 'r', 's']
                        ['t', 'u' ,'v']
                        m: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11,
                           36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47,
                           72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83,
                        n: 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23,
                           48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59,
                           84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95
                        o: 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35,
                           60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71,
                           96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107

                        p: 0, 1, 2,
                           12, 13, 14,
                           24, 25, 26,
                           36, 37, 38,
                           48, 49, 50,
                           60, 61, 62,
                           72, 73, 74,
                           84, 85, 86,
                           96, 97, 98,
                        q: 3, 4, 5
                           15, 16, 17,
                           27, 28, 29,
                           39, 40, 41,
                           51, 52, 53,
                           63, 64, 65,
                           75, 76, 77,
                           87, 88, 89,
                           99, 100, 101,
                        r: 6, 7, 8,
                           18, 19, 20,
                           30, 31, 32,
                           42, 43, 44,
                           54, 55, 56,
                           66, 67, 68,
                           78, 79, 80,
                           90, 91, 92,
                           102, 103, 104
                        s: 9, 10, 11,
                           21, 22, 23,
                           33, 34, 35,
                           45, 46, 47,
                           57, 58, 59,
                           69, 70, 71,
                           81, 82, 83,
                           93, 94, 95,
                           105, 106, 107
                        
                        ["jmpt","jmpu","jmpv","jmqt","jmqu","jmqv","jmrt","jmru","jmrv","jmst","jmsu","jmsv",
                         "jnpt","jnpu","jnpv","jnqt","jnqu","jnqv","jnrt","jnru","jnrv","jnst","jnsu","jnsv",
                         "jopt","jopu","jopv","joqt","joqu","joqv","jort","joru","jorv","jost","josu","josv",
                         "kmpt","kmpu","kmpv","kmqt","kmqu","kmqv","kmrt","kmru","kmrv","kmst","kmsu","kmsv",
                         "knpt","knpu","knpv","knqt","knqu","knqv","knrt","knru","knrv","knst","knsu","knsv",
                         "kopt","kopu","kopv","koqt","koqu","koqv","kort","koru","korv","kost","kosu","kosv",
                         "lmpt","lmpu","lmpv","lmqt","lmqu","lmqv","lmrt","lmru","lmrv","lmst","lmsu","lmsv",
                         "lnpt","lnpu","lnpv","lnqt","lnqu","lnqv","lnrt","lnru","lnrv","lnst","lnsu","lnsv",
                         "lopt","lopu","lopv","loqt","loqu","loqv","lort","loru","lorv","lost","losu","losv"]
                        """
                        """
                        2859
                        ['a', 'b', 'c']
                        ['t', 'u', 'v']
                        ['j', 'k', 'l']
                        ['w', 'x', 'y', 'z']

                        t: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11,
                           36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47,
                           72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83
                        u: 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23,
                           48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59,
                           84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95
                        v: 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35,
                           60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71,
                           96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107

                        j: 0, 1, 2, 3,
                           12, 13, 14, 15,
                           24, 25, 26, 27,
                           36, 37, 38, 39,
                           48, 49, 50, 51,
                           60, 61, 62, 63,
                           72, 73, 74, 75,
                           84, 85, 86, 87,
                           96, 97, 98, 99,
                        k: 4, 5, 6, 7,
                           16, 17, 18, 19,
                           28, 29, 30, 31,
                           40, 41, 42, 43,
                           52, 53, 54, 55,
                           64, 65, 66, 67,
                           76, 77, 78, 79,
                           88, 89, 90, 91,
                           100, 101, 102, 103
                        l: 8, 9, 10, 11,
                           20, 21, 22, 23,
                           32, 33, 34, 35,
                           44, 45, 46, 47,
                           56, 57, 58, 59,
                           68, 69, 70, 71,
                           80, 81, 82, 83,
                           92, 93, 94, 95,
                           104, 105, 106, 107

                        ["atjw","atjx","atjy","atjz","atkw","atkx","atky","atkz","atlw","atlx","atly","atlz",
                         "aujw","aujx","aujy","aujz","aukw","aukx","auky","aukz","aulw","aulx","auly","aulz",
                         "avjw","avjx","avjy","avjz","avkw","avkx","avky","avkz","avlw","avlx","avly","avlz",
                         "btjw","btjx","btjy","btjz","btkw","btkx","btky","btkz","btlw","btlx","btly","btlz",
                         "bujw","bujx","bujy","bujz","bukw","bukx","buky","bukz","bulw","bulx","buly","bulz",
                         "bvjw","bvjx","bvjy","bvjz","bvkw","bvkx","bvky","bvkz","bvlw","bvlx","bvly","bvlz",
                         "ctjw","ctjx","ctjy","ctjz","ctkw","ctkx","ctky","ctkz","ctlw","ctlx","ctly","ctlz",
                         "cujw","cujx","cujy","cujz","cukw","cukx","cuky","cukz","culw","culx","culy","culz",
                         "cvjw","cvjx","cvjy","cvjz","cvkw","cvkx","cvky","cvkz","cvlw","cvlx","cvly","cvlz"]
                        """

                        """
                        d: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11,
                           36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47,
                           72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83,
                           108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119
                        e: 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23,
                           48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59,
                           84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95,
                           120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131
                        f: 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35,
                           60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71,
                           96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107,
                           132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143

                        ["wdtp","wdtq","wdtr","wdts","wdup","wduq","wdur","wdus","wdvp","wdvq","wdvr","wdvs",
                         "wetp","wetq","wetr","wets","weup","weuq","weur","weus","wevp","wevq","wevr","wevs",
                         "wftp","wftq","wftr","wfts","wfup","wfuq","wfur","wfus","wfvp","wfvq","wfvr","wfvs",
                         "xdtp","xdtq","xdtr","xdts","xdup","xduq","xdur","xdus","xdvp","xdvq","xdvr","xdvs",
                         "xetp","xetq","xetr","xets","xeup","xeuq","xeur","xeus","xevp","xevq","xevr","xevs",
                         "xftp","xftq","xftr","xfts","xfup","xfuq","xfur","xfus","xfvp","xfvq","xfvr","xfvs",
                         "ydtp","ydtq","ydtr","ydts","ydup","yduq","ydur","ydus","ydvp","ydvq","ydvr","ydvs",
                         "yetp","yetq","yetr","yets","yeup","yeuq","yeur","yeus","yevp","yevq","yevr","yevs",
                         "yftp","yftq","yftr","yfts","yfup","yfuq","yfur","yfus","yfvp","yfvq","yfvr","yfvs",
                         "zdtp","zdtq","zdtr","zdts","zdup","zduq","zdur","zdus","zdvp","zdvq","zdvr","zdvs",
                         "zetp","zetq","zetr","zets","zeup","zeuq","zeur","zeus","zevp","zevq","zevr","zevs",
                         "zftp","zftq","zftr","zfts","zfup","zfuq","zfur","zfus","zfvp","zfvq","zfvr","zfvs"]
                        """
                        n = 1
                        for a in letters[idx+1:]:
                            n *= len(a)

                        combinations[didx + cidx*n] += l
                        didx += 1
                        if didx % n == 0:
                            didx += n*(len(letter)-1)
                            round_idx += 1
                        
                        if (idx == 1 and round_idx > len(letters[0]) - 1) or \
                            (idx == 2 and round_idx > len(letters[0]) * len(letters[1]) - 1):
                            cidx += 1
                            didx = 0
                            round_idx = 0
                    else:
                        combinations[duplicate+lidx] += l
        
        return combinations