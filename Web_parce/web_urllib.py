from urllib.request import urlopen
import re
page_ht= str(urlopen('https://ru.wikipedia.org/wiki/Python').read().decode('utf-8'))
page_html = page_ht.split()
print(page_ht.count('C++'))

ans = []
state = 0
for i in page_ht:
    if i == '<':
        state = 1
    if i == '>':
        state = 0
    elif state == 0:
        ans.append(i)


print()
page_sort = ''.join(ans)


print(page_sort.count('C++'))
# print(page_sort)
ans_word = 0
# for i in page_html:
#     print(i)

print(page_html.index('<body'))
print(page_html.index('</body></html>'))
slace_page = ''.join(page_html[186:22203])
print(slace_page.count('C++'))
