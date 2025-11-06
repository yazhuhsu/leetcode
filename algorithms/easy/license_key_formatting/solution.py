class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = s.replace('-', '')

        count = len(s) % k
        license_key, group, prefix = "", "", False
        if count == 0:
            prefix = True
        
        for c in s:
            group += c

            if not prefix and len(group) == count:
                license_key += group
                group, prefix = "", True

            if len(group) == k:
                if license_key != "":
                    license_key += "-"
                license_key += group
                group = ""

        return license_key.upper()

solution = Solution()
print(solution.licenseKeyFormatting("5F3Z-2e-9-w", 4) == "5F3Z-2E9W")
print(solution.licenseKeyFormatting("2-5g-3-J", 2) == "2-5G-3J")