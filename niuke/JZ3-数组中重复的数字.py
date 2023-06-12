from typing import List

print(1)




#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param numbers int整型一维数组
# @return int整型
#
class Solution1:
    def duplicate(self , numbers: List[int]) -> int:
        # write code here
        nset = set()
        for num in numbers:
            if num in nset:
                return num
            else:
                nset.add(num)
        return -1



if __name__=="__main__":
    Solution1().duplicate([1,2,3,1])
    print("main")
