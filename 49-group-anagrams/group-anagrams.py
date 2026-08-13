class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        wordDict = {}
        
        for word in strs:
            chars = [0] * 26 # a -> z

            for c in word:
                chars[ord(c) - ord('a')] += 1 # ord is ascii value

            key = tuple(chars)
            if key not in wordDict:
                wordDict[key] = []
            
            wordDict[key].append(word)


        return list(wordDict.values())