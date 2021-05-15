#include <regex>
regex r(R"(^[+-]?(\d+|\d+\.\d*|\.\d+)([eE][+-]?\d+)?$)");
class Solution {
public:
    bool isNumber(string s) {
        return regex_match(s, r);
    }
};
