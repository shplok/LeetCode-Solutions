import re
class Solution:
    def reorderSpaces(self, text: str) -> str:
        words = re.split(r'\s+', text.strip())
        gaps = len(words) - 1
        totalSpaces = 0

        for i in range(len(text)):
            if text[i] == " ":
                totalSpaces += 1

        if gaps == 0:
            return words[0] + " " * totalSpaces

        spaces = totalSpaces // gaps
        extraSpaces = totalSpaces % gaps

        result = ""
        for i in range(gaps):
            result += words[i] + ' ' * spaces
        result += words[-1] + ' ' * extraSpaces
        return result
