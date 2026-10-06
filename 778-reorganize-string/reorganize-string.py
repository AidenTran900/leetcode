from collections import Counter
import heapq

class Solution:
    def reorganizeString(self, s: str) -> str:
        freq = Counter(s)

        maxheap = [(-freq, char) for char, freq in freq.items()]
        heapq.heapify(maxheap)

        prev_freq = 0
        prev_char = ""
        
        ret = []

        while maxheap:
            freq, char = heapq.heappop(maxheap)
            ret.append(char)
            print(char)

            if -prev_freq > 0:
                heapq.heappush(maxheap, (prev_freq, prev_char))

            prev_freq = freq + 1 # add instead of sub since freqs are negative (max heap)
            prev_char = char

        result = "".join(ret)
        
        if len(result) == len(s):
            return result

        return ""
            
