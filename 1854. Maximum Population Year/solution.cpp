class Solution {
public:
    int maximumPopulation(vector<vector<int>>& logs) {
        map<int, int> population;
        
        for (auto& pair: logs) {
            for (int year = pair[0]; year < pair[1]; ++year) {
                population[year] += 1;
            }
        }
        
        int result = 1e6;
        int max_population = 0;
        
        for (const auto& iter: population) {
            if (iter.second > max_population) {
                result = iter.first;
                max_population = iter.second;
            }
        }
        
        return result;
    }
};
