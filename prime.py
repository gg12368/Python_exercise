编写一函数Prime(n)，对于已知正整数n，判断该数是否为素数，如果是素数，返回True,否则返回False。
(1)代码如下：
from math import sqrt
def prime(number):
    if number <= 1:
        return False
    else:
        ex = [i for i in range(2, round(sqrt(number) + 1)) 
            if number % i == 0]
        if ex:
            return False
        else:
            return True

pr = int(input("请输入正整数："))
if prime(pr):
    print("{}是素数".format(pr))
else:
print("{}不是素数".format(pr))
