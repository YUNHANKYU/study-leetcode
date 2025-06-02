def rob(nums: list[int]) -> int:
    max_2 = 0
    current = 0

    for i in nums:
        temp = current
        current = max(current, i + max_2)
        max_2 = temp

    print(current)
    return current


rob([7, 2, 3, 9, 1])
