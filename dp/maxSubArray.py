def maxSubArray(nums: list[int]) -> int:
    # 1. 순차적으로 순회하면서
    # 2. 현재 값 이전까지의 부분최대값과 현재값 비교해서 max 값 저장
    # 3. 그 값과 max_sum 값을 비교해서 max 값 저장
    # 4. 마지막 max_sum 값 return
    sub_max_sum = nums[0]
    max_sum = nums[0]

    for i in range(1, len(nums)):
        sub_max_sum = max(nums[i], sub_max_sum+nums[i])
        max_sum = max(max_sum, sub_max_sum)
    print(max_sum)
    return max_sum


def maxSubArrayDP(nums: list[int]) -> int:
    """
    DP 방식: dp[i] = i번째까지의 최대 연속 부분합
    각 위치에서 이전까지의 최대 부분합에 현재 값을 더할지, 아니면 현재 값부터 다시 시작할지 결정
    """
    if not nums:
        return 0
    n = len(nums)
    dp = [0] * n
    dp[0] = nums[0]
    max_sum = dp[0]
    for i in range(1, n):
        dp[i] = max(nums[i], dp[i-1] + nums[i])
        max_sum = max(max_sum, dp[i])
    print(max_sum)
    return max_sum

# 테스트 예시
maxSubArray([-1])
maxSubArray([5, 4, -1, 7, 8])
maxSubArrayDP([-2,1,-3,4,-1,2,1,-5,4])  # 6
maxSubArrayDP([-1])                     # -1
maxSubArrayDP([5, 4, -1, 7, 8])         # 23
