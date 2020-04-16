import re
import sqlite3

from urllib.request import urlopen
from html import unescape


def main():
	"""
	메인 처리입니다.
	fetch(), scrape(), save() 함수를 호출합니다.
	"""
	html = fetch('http://www.hanbit.co.kr/store/books/full_book_list.html')
	books = scrape(html)
	save = ('books.db',books)


def fetch(url):
	"""
	매개변수로 전달 받을 url을 기반으로 웹페이지를 추출합니다.
	웹 페이지의 인코딩 형식은 Content-Type 헤더를 기반으로 알아냅니다.
	반환값: str 자료형의 HTML
	"""
	f = urlopen(url)
	
	# HTTP 헤더를 기반으로 이코딩 형식을 추출합니다.
	encoding = f.info().get_content_charset(failobj="utf-8")

	# 추출한 인코딩 형식을 기반으로 문자열을 디코딩합니다.
	html = f.read().decode(encoding)
	return html

def scrape(html):
	"""
	매개변수 html로 받은 HTML을 기반으로 정규 표션식을 사용해 도서 정보를 추출합니다.
	반환값:도서 (dict) 리스트
	"""
	books = []
	# re.findall()을 사용해 도서 하나에 해당하는 HTML을 추출합니다.

	for partial_html in re.findall(r'<td class="left"><a.*?</td>',html, re.DOTALL()):
		# 도서의 URL을 추출합니다.
		url = re.search(r'<a href="(.*?)">' , partial_html).group()
		url = "http://www.hanbit.co.kr" + url

		# 태그를 제거해서 도서의 제목을 추출합니다.
		title = re.sub(r'<.*?>','',partial_html)
		title = unescape(title)
		books.append({'url':url, 'title':title})
	
	return books

def save(db_path, books):


