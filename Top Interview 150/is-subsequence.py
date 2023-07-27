class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        slow = 0
        fast = 0
        while fast < len(t) and slow < len(s):
            if s[slow] == t[fast]:
                fast += 1
                slow += 1
            else:
                fast += 1
        if slow == len(s):
            return True
        return False


