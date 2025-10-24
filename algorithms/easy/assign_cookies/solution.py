class Solution:
    def findContentChildren(self, g: list, s: list) -> int:
        g.sort()
        s.sort()
        
        success_count, failed_count = 0, 0
        success = False
        for i in range(len(g)):
            success, failed_count = False, 0
            for content in s:
                if content >= g[0]:
                    success_count += 1
                    s.remove(content)
                    success = True
                    break
                else:
                    failed_count += 1
            
            g.remove(g[0])

            if not success and failed_count == len(s):
                break

            if len(g) == 0:
                break

        return success_count

print(Solution().findContentChildren([1, 2, 3], [1, 1]) == 1)
print(Solution().findContentChildren([1, 2], [1, 2, 3]) == 2)