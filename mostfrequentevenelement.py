class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
                
        evenMap = {}
        
        for num in nums:
            if num % 2 == 0:
                if num in evenMap:
                    evenMap[num] += 1
                else:
                    evenMap[num] = 1

        max_freq = 0
        most_freq_even = -1

        for num, freq in evenMap.items():
            if freq > max_freq:
                max_freq = freq
                most_freq_even = num
            elif freq == max_freq:
                most_freq_even = min(most_freq_even, num)
            
        return most_freq_even
        
