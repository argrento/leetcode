class NumMatrix {
private:
    vector<vector<int>> m;    
public:
    NumMatrix(vector<vector<int>>& matrix) {
        m.assign(matrix.begin(), matrix.end());
    }
    
    int sumRegion(int row1, int col1, int row2, int col2) {
        int sum = 0;
        for (int row_idx = row1; row_idx <= row2; row_idx+=1) {
            for (int col_idx = col1; col_idx <= col2; col_idx+=1) {
                sum += m[row_idx][col_idx];
            }
        }
        return sum;
    }
};
