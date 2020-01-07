1.	编写程序解决爱因斯坦台阶问题：有人走一台阶，若以每步走两级则最后剩下一级；若每步走三级则剩两级；若每步走四级则剩三级；若每步走五级则剩四级；若每步走六级则剩五级；若每步走七级则刚好不剩。问台阶至少共有多少级？
(1)	源代码如下：
number = 7
a=b=c=d=e=0
while 1:
    a=number%2
    b=number%3
    c=number%4
    d=number%5
    e=number%6
    flag=(a==1)and(b==2)and(c==3)and(d==4)and(e==5)
    if flag:
        print("至少有%d级台阶"%number)
        break
else: number+=7
