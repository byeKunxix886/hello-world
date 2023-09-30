# _*_ coding : utf-8 _*_
# @Time : 2023/9/30 下午 03:56
# @Author : byeKun
# @File : test
# @Project : main.py

import urllib.request

url = "https://byekunxix886.github.io/MyStuff/"
response = urllib.request.urlopen(url)
content = response.read().decode('UTF-8')
print(content)

# <!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <title>byeKunResume</title>
# </head>
#
# <body>
#     <h1 draggable="true">Cheng Kun Cheng</h1>
#     <img src="./profile/me.jpg" height="250" width="200"/>
#     <hr/>
#     <p>I'm a senior programmer, being good at C language, Linux. Also, I got 119 in TOFELiBT.</p>
#     <hr/>
#
#     <h2>Education</h2>
#     <ul><li>Bachelor of Computer Science - Chin-Yi University of Technology(2021-2025)</li></ul>
#
#
#     <h2>Work experience</h2>
#     <br/>
#
#     <h2>Skills</h2>
#     <ul>
#         <li>HTML</li>
#         <li>C language</li>
#         <li>Python</li>
#         <li>web crawler</li>
#     </ul>
#     <p>There are no Awards, certifications, or other achievements (any relevant awards, certifications, or other accomplishments)</p>
#
#     <a href="https://github.com/byeKunxix886">Check my portfolio on GitHub</a>
#     <footer>Copyright © 2023 ChengKunCheng All Rights Reserved.</footer>
# </body>
# </html>











