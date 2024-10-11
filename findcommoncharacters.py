class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        
        countMap = {}

        for char in words[0]:
            countMap[char] = countMap.get(char, 0) + 1


            
        for word in words[1:]:
            charMap = {}
            

            for char in word:
                charMap[char] = charMap.get(char, 0) + 1

            for char in countMap:
                countMap[char] = min(countMap[char], charMap.get(char, 0))


        common_chars = []
        for char, count in countMap.items():
            common_chars.extend([char] * count)
        
        return common_chars