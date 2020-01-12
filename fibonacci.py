编写一函数Fabonacci(n)，其中参数n代表第n次的迭代。
(1)代码如下：
def fibonacci(num):
    fibs = [0,1]
    for i in range(num-2):
        #倒数第二个数+倒数第一个数的结果，追加到列表中
        fibs.append(fibs[-2]+fibs[-1])
    return(fibs)
print(fibonacci(10))
