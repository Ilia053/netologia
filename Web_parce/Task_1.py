from urllib.request import urlopen
from collections import Counter
from random import random
from bs4 import BeautifulSoup as Bs
page_html = str(urlopen('https://stepik.org/media/attachments/lesson/209719/2.html').read().decode('utf-8'))
page_html_list = page_html.split('</code>')
page_html_list_res = []
for i in page_html_list:
    if '<code>' in i:
        page_html_list_res.append(i[i.find('<code>') + len('<code>'):])

# print(page_html_list_res.sort())


# a = Counter(page_html_list_res)

a_set = set(page_html_list_res)
most_com = y = q = 0
most_list = []
while q != 3:
    for i in a_set:
        x = page_html_list_res.count(i)
        if x > y:
            y = x
            most_com = i
    most_list.append(most_com)
    a_set.discard(most_com)
    x = y = 0
    q+=1
print(most_list)

content_soup = Bs(page_html,'lxml')

print(content_soup)