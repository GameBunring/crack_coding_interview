# max array
def maxarray(nums, k):
    if not nums or k > len(nums):
        return []
    if k == 1:
        return nums
    
    res = [0] * len(nums)
    from collections import deque
    dq = deque()
    j = 0
    for i in range(len(nums)):
        if dq and dq[0] < i - k + 1:
            dq.popleft()
        while dq and nums[i] >= nums[dq[-1]]:
            dq.pop()
        dq.append(i)
        if i >= k - 1:
            j += 1
            res[j] = nums[dq[0]]
        
    while j < len(nums):
        if dq[0] < j:
            dq.popleft()
        j += 1
        res[j] = nums[dq[0]]
    return res
