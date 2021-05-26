class Solution {
public:
    int minPartitions(string n) {
        int result = '0';
        for (auto ch: n) {
            if (result < ch) {
                result = ch;
            }
        }
        
        return result - '0';
    }
};
