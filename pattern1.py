编写程序，用户输入一段英文，然后输出这段英文中所有长度为3个字母的单词。

import re
x = input('Please input a string:')
pattern = re.compile(r'\b[a-zA-Z]{3}\b')
print(pattern.findall(x))
