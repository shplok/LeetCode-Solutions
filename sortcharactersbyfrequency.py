class Solution:
    def frequencySort(self, s: str) -> str:
        charfrequency = {}

        for char in s:
            if char in charfrequency:
                charfrequency[char] += 1
            else:
                charfrequency[char] = 1

        sortedchars = sorted(charfrequency.items(), key=lambda x: x[1], reverse=True)

        sortedstr = ''

        for char, freq in sortedchars:
            sortedstr += char * freq

        return sortedstr
