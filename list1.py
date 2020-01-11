

有一段英文文本，其中有单词连续重复了2次，编写程序检查重复的单词并只保留一个。例如文本内容为“This is is a desk.”，程序输出为“This is a desk.”
a = input().split()
b = list() for i in a:  if i not in b:
        b.append(i) print(" ".join(b))
