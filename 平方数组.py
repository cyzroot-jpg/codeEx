"""
平方数组：一个有序的数组，经过对每个元素进行平方之后，依然保持有序的状态

建模：一个有序的数组平方后为无须的情况就是元素有负数的情况，又因为原来的数组已经是有序的，因此平方后应该是两边的元素大中间的元素小。
    同样，可以看作是在这个数组中挑选一个最大的放到新的数组里，而且我们只需要从第一个和最后一个进行比较即可。

暴力法：平方之后，进行快速排序，时间复杂度nlogn

双指针法：这个双指针法的核心思想，也是挑选元素放到新的数组里面，只不过这里用来挑选元素的指针有两个
"""

#双指针法：

def sortedSquares(self, nums: List[int]) -> List[int]:
        slow = len(nums) - 1
        newlist = [0]*len(nums)
        left = 0
        right = len(nums) - 1
        while left <= right:
            if nums[left] * nums[left] > nums[right]*nums[right]:
                newlist[slow] = nums[left] * nums[left]
                slow = slow - 1
                left = left + 1
            else:
                newlist[slow] = nums[right]*nums[right]
                slow = slow - 1
                right = right - 1
        return newlist