from typing import List


'''
在一个二维数组array中（每个一维数组的长度相同），每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
[
[1,2,8,9],
[2,4,9,12],
[4,7,10,13],
[6,8,11,15]
]
给定 target = 7，返回 true。

给定 target = 3，返回 false。

进阶：空间复杂度 O(1) ，时间复杂度 O(n+m)
'''



'''
    list有count方法， 表示 参数在list中出现的次数
'''


# 用 list的count方法
class Solution:
    def Find(self , target: int, array: List[List[int]]) -> bool:
        # write code here
        for row in range(len(array)):
            if array[row].count(target) > 0:
                return True
        return False

# 手写 二分查找
class Solution2:

    def binarySearch(self, target:int, array: List[int]) -> bool:
        if len(array) == 0:
            return False
        left = 0   # 左侧索引
        right = len(array) - 1   # 右侧索引

        while left <= right:
            mid = (int)((left + right) / 2)   #  或  (left + right) // 2
            if target < array[mid]:
                right = mid - 1
            elif target > array[mid]:
                left = mid + 1
            else:
                return True
        return False





    def Find(self, target: int, array: List[List[int]]) -> bool:
        # write code here
        for row in range(len(array)):
            if self.binarySearch(target, array[row]):
                return True
        return False








if __name__=="__main__":
    target = 7
    array = [[1,2,8,9],[2,4,9,12],[4,7,10,13],[6,8,11,15]]
    flag = Solution().Find(target, array)
    print(flag)
