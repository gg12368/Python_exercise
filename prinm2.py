利用上题中判断素数的函数，编写程序找出1~100 之间的所有孪生素数（若两个素数之差为2，则这两个素数就是一对孪生素数） 。例如：3 和5、5 和7、11和13 等都是孪生素数。
(1)代码如下：
from math import sqrt
# 判断一个数是否为素数
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
# 找1-100以内的孪生素数
def prime_twins():
    for i in range(1, 100):
        for j in range(2, 101):
            if prime(i) and prime(j) and j-i == 2:
                print(i, j)
prime_twins()
