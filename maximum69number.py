class Solution:
    def maximum69Number (self, num: int) -> int:
        
        numl = [int(dig) for dig in str(num)]
  
        for digit in range(len(numl)):
            if numl[digit] == 6:
                numl[digit] = 9
            
                break

        return int(''.join(map(str, numl)))
