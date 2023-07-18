class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        a = 0
        b = len(needle)
        if len(haystack) == b:
            return 0 if haystack == needle else -1
        while b <= len(haystack):
            if haystack[a:b] == needle:
                return a
            else:
                a += 1
                b += 1
        return -1