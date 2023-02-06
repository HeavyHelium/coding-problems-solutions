#include <vector>
#include <unordered_map>
#include <iostream>

int subarraySum(const std::vector<int>& nums, int k) {
    std::unordered_map<int, int> prefixes;

    int current_sum = 0;
    int cnt = 0;

    for(int i = 0; i < nums.size(); ++i) { 
        current_sum += nums[i];

        if(current_sum == k) { 
            ++cnt;
        }

        int temp = current_sum - k;
        if(prefixes.find(temp) != prefixes.end()) { 
            // you can ditch all prefixes with current_sum - k
            cnt += prefixes[temp]; // for subarray ending at i, the number increases with the # of all its prefixes with sum k - arr[i]
        }

        ++prefixes[current_sum];

    } 
    return cnt;
    
}


int main() { 

    int sum = -10;
    std::cout << subarraySum({ 10, 2, -2, -20, 10 }, sum) << std::endl;

    return 0;
}