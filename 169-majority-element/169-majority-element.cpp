class Solution {
public:
    int majorityElement(vector<int>& nums) {
        //O(1) space
        //O(n) time complexity
        // use dictionary(hashmap)
        int n = nums.size();
        int maj = n / 2;
        int ans = 0;
        map<int,int> map;
        for(int i = 0; i < n; i++) {
            if(map.find(nums[i]) ==  map.end()) {
                map.insert({nums[i], 1});
            } else {
                map[nums[i]]++;
            }
        }
        
        for(auto it:map){
            if(it.second > maj){
                ans = it.first;
            }
        }
        return ans;
    }
};