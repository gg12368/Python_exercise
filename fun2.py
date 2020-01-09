编写函数，可以接受任意多个整数并输出其中的最大值和所有整数之和。
(1)源代码如下：
def max_sum(num_list):
    sum_num = 0
    max_num = int(num_list[0])
    num_list = num_list.split(",")
    for i in range(len(num_list)):
        sum_num = sum_num + int(num_list[i])
        if(int(num_list[i]) > max_num):
            max_num = int(num_list[i])
    print('最大值是：',max_num)
    print('所有整数之和是：',sum_num)


num_list = input('请输入一些整数并以逗号隔开：')
max_sum(num_list)
