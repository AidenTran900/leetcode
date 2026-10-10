class Solution:
    def numDecodings(self, s: str) -> int:
        # naive
        # cases
            # 1 digit:
                # keep 2nd digit
                # skip
            # 2 digit
                # skip

        if s == '0':
            return 0

        if not s.isnumeric():
            return 0

        n = len(s)

        nxt = 1 # ways to decode after cur digit
        nxt2 = 0 # ways to decide after cur pair

        for i in range(n-1, -1, -1):
            # if the next digit is 0 then 1 digit impossible
            cur = nxt if s[i] != '0' else 0

            if (i < n-1) and (s[i] == '1' or s[i] == '2' and s[i+1] < '7'):
                cur += nxt2
            
            nxt2 = nxt
            nxt = cur

        return nxt
