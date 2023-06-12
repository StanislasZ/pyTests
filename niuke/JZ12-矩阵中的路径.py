from typing import  List

#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param matrix char字符型二维数组
# @param word string字符串
# @return bool布尔型
#
class Solution:

    visit = []

    def dfs(self, matrix, vis: List[List[bool]]):

    def hasPath(self , matrix: List[List[str]], word: str) -> bool:
        # write code here
        if len(matrix) == 0:
            return False
        n = len(matrix)
        m = len(matrix[0])
        visit = [[False for j in range(m)] for i in range(n)]




        print(        )

if __name__ == "__main__":
    matrix = [['a','b','c','e'],['s','f','c','s'],['a','d','e','e']]
    target = 'abcced'
    # flag = Solution().hasPath(matrix, target)
    # print(flag)

    visit = [[False for j in range(4)] for i in range(2)]
    print(visit)

