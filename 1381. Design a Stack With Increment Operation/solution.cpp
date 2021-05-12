class CustomStack {
private:
    int limit;
    vector<int> stack;
public:
    CustomStack(int maxSize) {
        limit = maxSize;
    }
    
    void push(int x) {
        if (stack.size() < limit) {
            stack.push_back(x);
        }
    }
    
    int pop() {
        if (stack.size() == 0) {
            return -1;
        } else {
            int ret_value = stack.back();
            stack.pop_back();
            return ret_value;
        }
    }
    
    void increment(int k, int val) {
        for (int idx = 0; idx < k and idx < stack.size(); idx += 1) {
            stack[idx] += val;
        }
    }
};
