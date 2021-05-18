class Solution {
public:
    vector<vector<string>> findDuplicate(vector<string>& paths) {
        vector<vector<string>> result;
        unordered_map<string, vector<string>> duplicates;
        
        for (auto path: paths) {
            stringstream ss(path);
            string token, basePath, fileName, fileContents;
            
            ss >> basePath;
            
            while (ss >> token) {
                size_t contentsStart = token.find('(');
                fileName = token.substr(0, contentsStart);
                fileContents = token.substr(contentsStart);
                duplicates[fileContents].push_back(basePath + '/' + fileName);
            }
            
        }
        
        for (auto duplicate : duplicates) {
            if (duplicate.second.size() > 1)
                result.push_back(duplicate.second);
        }

        return result;
    }
};
