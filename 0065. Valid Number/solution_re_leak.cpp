#include <regex>
class Solution {
public:
    bool isNumber(string s) {
        regex r(R"(^[+-]?(\d+|\d+\.\d*|\.\d+)([eE][+-]?\d+)?$)");
        return regex_match(s, r);
    }
};
