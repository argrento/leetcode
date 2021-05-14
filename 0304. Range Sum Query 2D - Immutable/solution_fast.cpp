class NumMatrix {
private:
    vector<vector<int>> sums;    
public:
    NumMatrix(vector<vector<int>>& matrix) {
        int r_size = matrix.size();
        int c_size = matrix[0].size();
        
        sums = vector<vector<int>>(r_size+1, vector<int>(c_size+1, 0));
        
        for (int i = 1; i <= r_size; i += 1) {
            for (int j = 1; j <= c_size; j += 1) {
                sums[i][j] = matrix[i-1][j-1] +
                             sums[i-1][j] +
                             sums[i][j-1] -
                             sums[i-1][j-1];
            }
        }
    }
    
    int sumRegion(int row1, int col1, int row2, int col2) {
        return sums[row2+1][col2+1] - sums[row2+1][col1] - sums[row1][col2+1] + sums[row1][col1]; 
    }
};
