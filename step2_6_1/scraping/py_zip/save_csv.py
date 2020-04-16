import csv


# 파일을 엽니다. newline=''으로 줄바꿈 코드의 자동 변환을 제어합니다. 
with open('top_cities.csv','w',newline='') as f :
	# CSV.writer는 파일 객체를 매개변수로 지정합니다.
	writer = csv.writer(f)

	# 첫번째 줄에는 헤더를 작성합니다.
	writer.writerow(['rank','city','population'])
	# writerrows()에 리스트를 전달하면 여러 개의 값을 출력합니다.
	writer.writerows([
		[1,'상하이',24150000],
		[2,'일본',5213500],
		[3,'서울',5899333],
		[4,'독도',339716],
	])
	
