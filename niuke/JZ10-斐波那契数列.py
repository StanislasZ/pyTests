#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param n int整型
# @return int整型
#
class Solution:

    fib = [0, 1, 2]

    def Fibonacci(self , n: int) -> int:
        if n == 1:
            return 1
        elif n == 2:
            return 1
        else:
            for i in range(3, n + 1):
                self.fib.append(self.fib[i - 2] + self.fib[i - 1])
        return self.fib[n]

    def Fibonacci2(self, n: int) -> int:
        # write code here
        a = 1
        b = 1
        if n == 1:
            return a
        elif n == 2:
            return b
        else:

            for i in range(3, n + 1):
                c = a + b
                a = b
                b = c

        return b



if __name__ == "__main__":
    for i in range(3, 5):
        print(i)