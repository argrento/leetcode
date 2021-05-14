class Solution {
public:
    vector<int> nextGreaterElement(vector<int>& nums1, vector<int>& nums2) {
        vector<int> result;
        for (int num1: nums1) {
            auto it = find(nums2.begin(), nums2.end(), num1);
            int greaterElement = -1;
            for (auto it2 = it; it2 < nums2.end(); it2 += 1) {
                if (*it2 > num1) {
                    greaterElement = *it2;
                    break;
                }
            }
            result.push_back(greaterElement);
        }
        
        return result;
    }
};
