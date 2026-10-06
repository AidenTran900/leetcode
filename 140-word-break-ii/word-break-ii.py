class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> list[str]:
        n = len(s)
        if n == 0:
            return []


        sentences = []
        def recurse(result, start_idx):
            if start_idx == n:
                sentences.append(" ".join(result))
                return

            for word in wordDict:
                matches = True

                for i, char in enumerate(word):
                    if (start_idx + i) >= n or s[start_idx + i] != char:
                        matches = False
                        break

                if matches:  
                    recurse(result + [word], start_idx + len(word))
                

        recurse([], 0)

        return sentences