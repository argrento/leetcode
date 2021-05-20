class Solution {
public:
    vector<vector<int>> levelOrder(TreeNode* root) {
        vector<vector<int>> result;
        queue<TreeNode*> q;
        
        if (!root) {
            return result;
        }
        q.push(root);
        
        while (!q.empty()) {
            int nodesNumber = q.size();
            vector<int> level;
            for (int nodeId = 0; nodeId < nodesNumber; nodeId+=1) {
                TreeNode* node = q.front();
                q.pop();
                level.push_back(node->val);
                
                if (node->left) {
                    q.push(node->left);
                }
                
                if (node->right) {
                    q.push(node->right);
                }
            }
            result.push_back(level);
        }
        
        return result;
    }
};
