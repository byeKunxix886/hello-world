# _*_ coding : utf-8 _*_
# @Time : 2023/9/29 下午 01:57
# @Author : byeKun
# @File : PythonSyntax
# @Project : main.py

# 直接在內容裡加空格並不會有影響，要連結字串+' '才會有空格
# Python會自動print裡加入\n，所以不要讓print自動換行就將\n拿掉即可
# print(, end= ' ')將它留白
for i in range(5):
    print('Hi I,m KunCheng. ', end='')
print()

str1 = 'MyNameisKun'
for i in str1:
    print(i,end='')
print()

list1 = ['Hi',"I'm",'KunCheng']
for i in list1:
    print(i+' ',end='')
print()







