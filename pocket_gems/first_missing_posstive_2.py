# first missing positive
def firstMissingPossitive(nums):
    if not nums:
        return 1

    for i in range(len(nums)):
        if nums[i] == i + 1:
            continue
        while nums[i] > 0 and nums[i] <= len(nums):
            print(i)
            print(nums)
            if nums[i] == nums[nums[i] - 1]:
                break
            test = nums[i] - 1
            nums[i], nums[test] = nums[test], nums[i]
            print(nums)
            
    for i in range(len(nums)):
        if nums[i] != i + 1:
            return i + 1
    return len(nums) + 1

print(firstMissingPossitive([5,3,2,2,1,5,6]))