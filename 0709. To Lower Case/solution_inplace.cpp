class Solution {
public:
    string toLowerCase(string s) {
        for (auto& ch: s) {
            if (ch >= 'A' && ch < 'a') {
                ch += ' ';
            }
        }
        return s;
    }
};
