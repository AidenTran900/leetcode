class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        def recurse(string, memory):
            if string in memory:
                return memory[string]

            if not string:
                return True

            for word in wordDict: # O(d)
                if string.startswith(word):
                    substring = string[len(word):] # O(k)

                    if recurse(substring, memory):
                        memory[string] = True
                        return True

            memory[string] = False
            return False

        return recurse(s, {})