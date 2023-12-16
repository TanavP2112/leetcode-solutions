# before anything, make sure to trim all the whitespace at the beginning and end of each string.
# then, you split the sentence into words using the split method, which stores it in an array.
# from there, you know the index of the last word is -1 and you use len to find the length.

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s.strip()
        s = s.split()
        return len(s[-1])