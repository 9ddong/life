#!python
print("Content-Type: text/html")
print()
#한글 깨짐 현상 방식
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')
import cgi, os
#목록
files = os.listdir('data')
listStr=''
for item in files:
    listStr = listStr + '<li><a href="index.py?id={name}">{name}살</a></li>'.format(name=item)
#query String
form = cgi.FieldStorage()
if 'id' in form:
    pageId = form["id"].value
    description = open('data/'+pageId, 'r', encoding='utf-8').read()
else:
    pageId = ""
    description = open('table', encoding='utf-8').read()

print('''<!doctype html>
<html>
  <head>
    <title>박준언의 인생</title>
    <meta charset="utf-8">
    <link href="style.css" rel="stylesheet">
  </head>

  <body>
    <img src="pictures\배너.jpg">
    <a href="index.py"><h1 class="top">박준언의 인생</h1></a>
    <div id="grid">
      <ul>
        {listStr}
      </ul>
      <div>
          <h2>{title}살</h2>
          <p class="comments">{desc}</p>
          <a href="create.py?id={title}">글 추가</a>
      </div>
    </div>
  </body>
  </html>
  '''.format(title=pageId, desc=description, listStr=listStr))
