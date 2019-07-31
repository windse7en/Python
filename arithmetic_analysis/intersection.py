import math

'''
To find the root of formula by intersection ways.
如果某种特殊情况会造成来回摇摆。
1. 坡度递减，
 y = ax, a = (delta y / delta x) = (f(x1) - f(x0)) / (x1 - x0)
 x2 = x1 - y1 / a
'''
def intersection(function,x0,x1): #function is the f we want to find its root and x0 and x1 are two random starting points
    x_n = x0
    x_n1 = x1
    while True:
        x_n2 = x_n1-( function(x_n1) / ( (function(x_n1)-function(x_n) ) / (x_n1-x_n) ))
        if abs(x_n2 - x_n1) < 10**-5:
            return x_n2
        x_n=x_n1
        x_n1=x_n2

def f(x):
    return math.pow(x , 3) - (2 * x) -5

if __name__ == "__main__":
    print(intersection(f,3,3.5))
