#leecode 209
"""
长度最小的子数组：给定一个含有 n 个正整数的数组和一个正整数 target 。找出该数组中满足其总和大于等于 target 的长度最小的子数组，返回它的长度

建模：一个快指针构建子数组，慢指针遍历
"""

#双指针法：
def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        s = 0
        sum = 0
        leng = 0
        result = 100000000000000
        for i in range(len(nums)):
            sum = sum + nums[i]
            while sum >= target:
                leng = i - s + 1
                if leng <= result:
                    result = leng
                sum = sum - nums[s]
                s = s + 1
        if leng == 0:
            result = 0
        return result