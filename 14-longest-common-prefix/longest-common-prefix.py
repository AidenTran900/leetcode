class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0: 
            return ""
        if len(strs[0]) == 0: 
            return ""

        index = 0
        prevChar = strs[0][0]

        prefix = ""

        while True:
            if index > len(strs[0]) - 1:
                    return prefix

            prevChar = strs[0][index]
            for string in strs:
                if index > len(string) - 1:
                    return prefix

                curChar = string[index]

                if prevChar != curChar:
                    return prefix
            

            prefix += prevChar
            index += 1

        return prefix

