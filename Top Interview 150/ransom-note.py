class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        map = {}
        for char in ransomNote:
            if char in map:
                map[char] += 1
            else:
                map[char] = 1
        for char2 in magazine:
            if map.get(char2, 0):
                map[char2] -= 1
                if map[char2] == 0:
                    map.pop(char2)
        if not map:
                return True
        return False
