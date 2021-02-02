from urllib.request import urlopen
import re
page_ht= str(urlopen('https://stepik.org/media/attachments/lesson/209717/1.html').read().decode('utf-8'))
page_html = page_ht.splitlines()
new_page = re.split('<body>','</body>',page_ht)
print(type(page_html))

print(page_ht.find('<body/>'))
print(page_html[-1])

print('I did everthing!')
