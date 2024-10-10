class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list) # mapping char count to list of anagrams

        for s in strs:
            count = [0] * 26 # a ..... z

            for c in s:
                count[ord(c) - ord("a")] += 1
                # ord takes one character and returns the unicode value for that char
            result[tuple(count)].append(s)

        return result.values()