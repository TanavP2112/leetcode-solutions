var twoSum = function(nums, target) {
    map = new Map();
    for (i = 0; i < nums.length; i++) {
        map.set(target - nums[i], i);
        if (target - nums[i] in map) {
            return [map[target - nums[i]], i];
        }
        map[nums[i]] = i
    }
    return [];
}