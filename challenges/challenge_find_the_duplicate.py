def find_duplicate(nums):
    if not isinstance(nums, list) or len(nums) < 2:
        return False

    if any(not isinstance(num, int) or num < 1for num in nums):
        return False

    nums.sort()

    for i in range(len(nums) - 1):
        if nums[i] == nums[i + 1]:
            return nums[i]

    return False
