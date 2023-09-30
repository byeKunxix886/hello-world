# _*_ coding : utf-8 _*_
# @Time : 2023/9/30 下午 03:56
# @Author : byeKun
# @File : test
# @Project : URLLIB.py

#練習1：從網頁響應一層一層剝再解碼獲取網頁的源碼
import urllib.request

url = "https://byekunxix886.github.io/MyStuff/"
response = urllib.request.urlopen(url)
content = response.read().decode('UTF-8')
print(content)

#練習2：1個類型，6個方法

print(type(response)) #網頁響應的類型是HTTPResponse

content = response.read() #按照一字節一字節的讀，速度較慢
print(content)

content = response.readline() #讀取一行字節(僅一行)

content = response.readlines() #讀取一行行直到結束，但是會以list的形式返回，以至於不能夠使用decode。
#問題：該如何解決無法使用DECODE呢？ 這樣返回來的都是二進制

content = response.getcode() #返回狀態碼，如果值是200則正確

content = response.geturl() #返回URL地址









