# next pumutation
def nextPumutation(nums):
    if not nums or len(nums) == 1:
        return
    for i in range(2, len(nums) + 1):
        if nums[-i] < nums[-i + 1]:
            swap_index = -i + 1
            for j in range(swap_index, 0):
                if nums[-i] < nums[j] < nums[swap_index]:
                    swap_index = j
            nums[-i], nums[swap_index] = nums[swap_index], nums[-i]
            break
    
    nums[-i + 1:] = list(reversed(nums[-i + 1:]))

a = [1,2,7,3,2]
nextPumutation(a)
print(a)
    
        