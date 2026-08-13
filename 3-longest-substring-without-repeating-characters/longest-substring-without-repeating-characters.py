class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dupeSet = set()

        start = 0
        longest = 0
        for end in range(len(s)):
            c = s[end]
            
            while c in dupeSet:
                dupeSet.remove(s[start])
                start += 1
            
            dupeSet.add(c)
            longest = max(longest, end - start + 1)

        return longest