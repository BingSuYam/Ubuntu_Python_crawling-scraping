import requests
import lxml.html

response = requests.get('https://www.hanbit.co.kr/store/books/new_book_list.html')
root = lxml.html.fromstring(response.content)
for a in root.cssselect('.view_box .book_tit a'):
    url = a.get('href')
    print(url)

