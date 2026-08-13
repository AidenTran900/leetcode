class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1

        s = s.lower()

        while i < j:
            charI = s[i]
            charJ = s[j]

            if not charI.isalnum(): 
                i += 1
                continue

            if not charJ.isalnum(): 
                j -= 1
                continue

            if charI != charJ: 
                return False

            i += 1
            j -= 1

        return True