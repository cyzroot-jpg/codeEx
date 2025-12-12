#二分法
"""
二分法：通过对半划分区间查找target，前提是有序数组

边界的处理：
1.闭区间：[left, right]
2.开区间：[left, right)
"""

#闭区间写法:
def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            midle = (left + right) // 2
            if nums[midle] > target:
                right = midle - 1
            elif nums[midle] < target:
                left = midle + 1
            else:
                return midle
        return -1

#开区间写法:
def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)
        while left < right:
            midle = (left + right) // 2
            if nums[midle] > target:
                right = midle
            elif nums[midle] < target:
                left = midle + 1
            else:
                return midle
        return -1