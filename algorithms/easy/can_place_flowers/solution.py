class Solution:
    def canPlaceFlowers(self, flowerbed: list, n: int) -> bool:
        if len(flowerbed) == 1:
            return (flowerbed[0] == 0 and n<=1) or (flowerbed[0]==1 and n==0)
        
        count = 0
        for idx, bed in enumerate(flowerbed):
            if idx == 0:
                if bed == 0 and flowerbed[1] != 1:
                    count += 1
                    flowerbed[0] = 1
                continue

            if idx == len(flowerbed)-1:
                if bed == 0 and flowerbed[idx-1]==0:
                    count += 1
                    flowerbed[idx] = 1
                continue

            if bed == 0 and flowerbed[idx-1] == 0 and flowerbed[idx+1] == 0:
                count += 1
                flowerbed[idx] = 1

        if n <= count:
            return True

        return False

solution = Solution()
print(solution.canPlaceFlowers([1,0,0,0,1], 1)==True)
print(solution.canPlaceFlowers([1,0,0,0,1], 2)==False)