#first missing positive
def first_missint_possitive(nums):
    if not nums:
        return 1
    upper = len(nums) - 1
    lower = 0
    while lower < upper:
        i = (lower + upper) // 2 + 1
        if nums[i] == i + 1:
            lower = i
        else:
            upper = i - 1
    return lower + 1
    

print(first_missint_possitive([1,2,3,6,7,9]))