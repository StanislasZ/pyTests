from typing import List

'''
描述
请实现一个函数，将一个字符串s中的每个空格替换成“%20”。
例如，当字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy。

。保证字符串中的字符为大写英文字母、小写英文字母和空格中的一种
'''


class Solution:
    def replaceSpace2(self, s: str) -> str:
        return s.replace(" ", "%20")

    def replaceSpace(self, s: str) -> str:
        # write code here
        s2 = ''
        for c in s:
            if c == ' ':
                s2 = s2 + '%20'
            else:
                s2 = s2 + c
        return s2


if __name__ == "__main__":
    s2 = Solution().replaceSpace2('We Are Happy')
    print(s2)
