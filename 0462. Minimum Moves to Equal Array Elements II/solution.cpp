class Solution {
public:
    int minMoves2(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        
        int result = 0;
        int median = 0;
        median = nums[nums.size() / 2];
        
        for (int num: nums) {
            result += abs(median - num); 
        }
        
        return result;
    }
};
