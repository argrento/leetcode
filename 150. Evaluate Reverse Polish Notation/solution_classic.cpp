class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        vector<int> stack;
        string ops = "+-*/";
        for (auto const& token: tokens) {
            cout << token;
            if (ops.find(token) == string::npos) {
                stack.push_back(stoi(token));
            } else {
                int right_op = stack.back();
                stack.pop_back();
                int left_op = stack.back();
                stack.pop_back();
                
                if (token == "+") {
                    stack.push_back(left_op + right_op); 
                } else if (token == "-") {
                    stack.push_back(left_op - right_op); 
                } else if (token == "*") {
                    stack.push_back(left_op * right_op); 
                } else if (token == "/") {
                    stack.push_back(left_op / right_op); 
                } 
                    
            }
        }
        
        return stack[0];
    }
};
