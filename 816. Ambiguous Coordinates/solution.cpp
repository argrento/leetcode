class Solution {
public:
    vector<string> gen(string s) {
        int length = s.size();
        if (length == 0 || (length > 1 && s[0] == '0' && s[length-1] == '0')) {
            return {};
        }
        if (s[0] == '0' && length > 1) {
            return {"0." + s.substr(1)};
        }
        if (s[length-1] == '0' || length == 1) {
            return {s};
        }
        vector<string> result = {s};
        for (int i = 1; i < length; ++i) {
            result.push_back(s.substr(0, i) + '.' + s.substr(i));
        }
        return result;
    }  
    
    vector<string> ambiguousCoordinates(string s) {
        int length = s.size();
        vector<string> result;
        
        for (int i = 1; i < length-2; ++i) {
            vector<string> left = gen(s.substr(1, i));
            vector<string> right = gen(s.substr(i + 1, length - 2 - i));
            
            for (auto& a: left) {
                for (auto& b: right) {
                    result.push_back("(" + a + ", " + b + ")");
                }
            }
        }
        
        return result;
    }
};
