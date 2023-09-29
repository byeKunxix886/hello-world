# _*_ coding : utf-8 _*_
# @Time : 2023/9/29 下午 01:57
# @Author : byeKun
# @File : PythonSyntax
# @Project : main.py

# print直接在內容裡加空格並不會有影響，要連結字串+' '才會有空格
# Python會自動print裡加入\n，所以不要讓print自動換行就將\n拿掉即可
# print(, end= ' ')將它留白

'''
for 變量 in 要遍歷的數據:
 	內容

有三種方式
1.range
(1)range(5) (0,5)0~4 此方法的結果是一個可以遍歷的對象 左閉右開區間
(2)range(1,3) (起始值,結束值)
(3)range(1,10,3) (起始值,結束值,步長)
2.循環一字符串
3.循環一列表
*遍歷列表中的下標
'''
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







