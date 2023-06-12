from typing import  List

#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param rotateArray int整型一维数组
# @return int整型
#
class Solution:
    def minNumberInRotateArray(self , rotateArray: List[int]) -> int:
        # write code here
        left = 0
        right = len(rotateArray) - 1
        while left < right:
            mid = int((left + right) / 2)
            if rotateArray[mid] > rotateArray[right]:
                left =  mid + 1
            elif rotateArray[mid] < rotateArray[right]:
                right = mid
            else:
                # 相同
                right = right -1
        return rotateArray[left]


if __name__ == "__main__":
    Solution().minNumberInRotateArray([3,4,5,1,2])