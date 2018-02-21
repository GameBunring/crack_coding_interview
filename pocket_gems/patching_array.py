import bisect

# patching array
def minPatches(nums, n):
    res, cur, i = 0, 1, 0
    while cur <= n:
        if i < len(nums) and nums[i] <= cur:
            cur += nums[i]
            i += 1
        else:
            cur *= 2
            res += 1
    return res
                
print(minPatches([1,2], 20))