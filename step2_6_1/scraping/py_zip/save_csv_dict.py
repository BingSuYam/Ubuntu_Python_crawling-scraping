import csv


with open('top_cities.csv','w',newline='') as f :
	# 첫번째 매개변수에 파일 객체
	# 두번째 매개변수에 필드 이름 리스트를 지정합니다.
	writer = csv.DictWriter(f,['rank','city','population'])
	writer.writeheader()
	# writerows()로 여러 개의 데이터를 딕셔너리 형태로 작성합니다.
	writer.writerows([
		{'rank':1 , 'city': '상하이' , 'population':24150000},
		{'rank':2 , 'city': '가나' , 'population':34150000},
		{'rank':3 , 'city': '일본' , 'population':44150000},
		{'rank':4 , 'city': '몽골' , 'population':54150000},
		{'rank':5 , 'city': '태국' , 'population':64150000},
		{'rank':6 , 'city': '이탈리아' , 'population':74150000},
	])
