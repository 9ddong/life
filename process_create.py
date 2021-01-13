#!python
import cgi
form = cgi.FieldStorage()
Id = form['id'].value
content = form['content'].value

opened_file = open('data/'+Id, 'w', encoding='utf-8')
opened_file.write(content)
opened_file.close()

print("Location: index.py?id="+Id)
print()
