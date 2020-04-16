import re
from html import unescape

# 이전 절에서 다운로드한 파일을 열고 html 이라는 변수에 저장합니다ㅣ. 

with open('dp.html') as f :
	html = f.read()

# re.findall()을 사용해 도서 하나에 해당하는 html을 추출합니다ㅣ. 



for partial_html in re.findall (r'<td class="left"><a.*?</td>',html, re.DOTALL):
	
	print ('---------------------------')
	print (partial_html)
	print ('---------------------------')



	#도서의 URL을 추출합니다.
	url = re.search(r'<a href="(.*?)">', partial_html)
	print ('-------------url--------------')
	print (url)
	print ('---------------------------')

	url = url.group(1)
	url = 'http://www.hanbit.co.kr' + url

	# 태그를 제거해서 도서의 제목을 추출합니다.
	title = re.sub(r'<.*?>','',partial_html)
	title = unescape(title)
	print ('url:',url)
	print ('title : ', title)
	print ('----------------')




