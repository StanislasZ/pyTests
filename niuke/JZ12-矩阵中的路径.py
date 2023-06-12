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

    def dfs(self, matrix: List[List[str]], n: int, m: int, i: int, j: int, word: str, k: int,
            flag: List[List[bool]]) -> bool:
        if i < 0 or i >= n or j < 0 or j >= m or (matrix[i][j] != word[k]) or flag[i][j]:
            # 下标越界、字符不匹配、已经遍历过不能重复
            return False
        # k为记录当前第几个字符
        if k == len(word) - 1:
            return True
        flag[i][j] = True
        # 该结点任意方向可行就可
        if (self.dfs(matrix, n, m, i - 1, j, word, k + 1, flag)
                or self.dfs(matrix, n, m, i + 1, j, word, k + 1, flag)
                or self.dfs(matrix, n, m, i, j - 1, word, k + 1, flag)
                or self.dfs(matrix, n, m, i, j + 1, word, k + 1, flag)):
            return True
        # 没找到经过此格的，此格未被占用
        flag[i][j] = False
        return False

    def hasPath(self, matrix: List[List[str]], word: str) -> bool:
        if len(matrix) == 0:
            return False
        n = len(matrix)
        m = len(matrix[0])
        # 初始化flag矩阵记录是否走过
        flag = [[False for i in range(m)] for j in range(n)]
        # 遍历矩阵找起点
        for i in range(n):
            for j in range(m):
                # 通过dfs找到路径
                if self.dfs(matrix, n, m, i, j, word, 0, flag):
                    return True
        return False

if __name__ == "__main__":
    matrix = [['a','b','c','e'],['s','f','c','s'],['a','d','e','e']]
    target = 'abcced'
    flag = Solution().hasPath(matrix, target)
    print(flag)



