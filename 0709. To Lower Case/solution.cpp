class Solution {
public:
    string toLowerCase(string s) {
        stringstream result;
        for (auto ch: s) {
            char tmp = ch;
            if (ch >= 'A' && ch < 'a') {
                tmp += ' ';
            }
            result << tmp;
        }
        
        return result.str();
    }
};
