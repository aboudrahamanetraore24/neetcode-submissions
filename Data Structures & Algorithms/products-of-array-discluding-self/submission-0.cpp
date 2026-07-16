#include <vector>

class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int n = nums.size();
        std::vector<int> prefix(n,1);
        std::vector<int> suffix(n,1);
        for(int i=1;i<n;i++) {
            prefix[i]=prefix[i-1]*nums[i-1];
        }
        for(int i=1;i<n;i++){
            suffix[n-1-i] = suffix[n-i]*nums[n-i];
        }
        std::vector<int> out(n);
        for(int i = 0;i<n;i++) {
            out[i] = prefix[i]*suffix[i];
        }
        return out;
    }
};
