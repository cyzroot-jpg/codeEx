#leecode 27
"""
移除不需要的元素：移除的目标值为3，将数组中的3移除，返回新数组的长度

建模：建模为在一个数组中挑选非目标值的元素，并更新到新数组中
"""

#双指针法：快指针：用于挑选非目标值 慢指针：新数组的下标
def removeElement(self, nums: List[int], val: int) -> int:
        slow = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[slow] = nums[i]
                slow = slow + 1
        return slow