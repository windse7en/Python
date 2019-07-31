import numpy as np
import math

'''
学到了
1. 用function的方法来传递函数，这样bisection，二分法的效果就会更好，更general。
2. 中间对于function（mid）的验证可以去掉，因为本身的条件回回归到最后的位置,没有影响去掉了也可以。
3. 用while loop的方式来去递归，这样就不会有栈溢出的问题。
'''

def bisection(function, a, b):
    if function(a) == 0:
        return a
    elif function(b) == 0:
        return b
    elif function(a) * function(b) > 0:
        print(f"Sorry, no result between{a} and {b}")
        return
    else:
        mid = (a + b) / 2.0
        times = 0
        while abs(a - mid) > 10**-7:
            times += 1
            if function(a) * function(mid) < 0:
                b = mid
            else:
                a = mid
            mid = (a + b) / 2.0
        print(f"{a} and {b} iteration {times} times")
        return mid

def test_zero(v):
    return v

def f(x):
    return math.pow(x, 3) - 2*x - 5

print(bisection(test_zero, -1, 100))
