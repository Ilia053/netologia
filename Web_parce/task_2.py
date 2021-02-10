from urllib.request import urlopen, urlretrieve
from bs4 import BeautifulSoup as Bs
import requests as req
from lxml import html

content = req.get('https://lk.megafon.ru/login/')
soup = Bs(content.text, 'lxml')
print(soup.script)
scr_soup = ''.join(soup.script)
print(scr_soup.find('{'))
print(scr_soup.find('}'))
sl_scr_soup = scr_soup[23:758]
print(sl_scr_soup.split(','))
lis_sl_scr_soup = sl_scr_soup.split(',')

print(len(lis_sl_scr_soup))
special_dict = dict.fromkeys(range(1,len(lis_sl_scr_soup)), 0)
i =  y = 0; x = 1

while i != len(lis_sl_scr_soup):
    special_dict[x] = lis_sl_scr_soup[y]
    x+=1;y+=1;i+=1
print(special_dict)



resp = urlopen('https://stepik.org/media/attachments/lesson/245130/6.html')
html = resp.read().decode('utf8')
soup = Bs(html, 'html.parser')
table = soup.find('table', attrs = {'class' : 'wikitable sortable'})
print(table)
cnt = 0
for tr in soup.find_all('tr'):
    cnt += 1
    for td in tr.find_all(['td', 'th']):
        cnt *= 2
print(cnt)

