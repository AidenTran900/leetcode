class Solution {
public:
    unordered_map<char, char> CLOSE_MAP = {
        {')', '('},
        {'}', '{'},
        {']', '['}
    };

    bool isValid(string string) {
        unsigned int stringLen = string.length(); // String len is never negative so unsigned
        if (stringLen <= 1) { return false; } // String len <= 1 is never valid
        stack<char> openedChar;

        for (unsigned int i = 0; i < stringLen; i++) {
            char character = string[i];

            // Check if character is closed
            if (CLOSE_MAP.count(character)) {
                // Check if the open stack is empty / doesn't match the closed bracket
                if (openedChar.empty() || openedChar.top() != CLOSE_MAP[character]) {
                    return false;
                }
                openedChar.pop();
            } else {
                openedChar.push(character);
            }
        }

        return openedChar.empty(); // Invalid if there are remaining brackets
    }
};