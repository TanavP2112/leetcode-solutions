class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        str = ""
        for i in range(min(len(word1), len(word2)) + 1):
            if i == len(word1):
                str += word2[i:]
            elif i == len(word2):
                str += word1[i:]
            else:
                str += word1[i] + word2[i]
        return str