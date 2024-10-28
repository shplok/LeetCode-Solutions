class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        return True if ransomNote in magazine else False
        