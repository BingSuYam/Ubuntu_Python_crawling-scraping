import sqlite3

# top_cities.db 파일을 열고 연결을 변수에 저장합니다.
conn = sqlite3.connect('top_cities.db')


# 커서를 추출합니다.
c = conn.cursor()


# excute() 메서드로 SQL 구문을 실행합니다.
# 스크립트를 여러 번 사용해도 같은 결과를 출력할 수 있게 cities 테이블이 존재하는 경우 제거합니다.

c.execute('DROP TABLE IF EXISTS cities')

# cities 테이블을 생서합니다.
c.execute('''
	CREATE TABLE cities(
		rank integer,
		citiy text,
		pop integer
	)
''')


# excute() 메서드의 두 번째 매개변수에는 파라미터를 지정할 수 있습니다.
# SQL 내부에서 파라미터로 변경할 부분(플레이스홀더)는 ?로 지정합니다.
c.execute('INSERT INTO cities VALUES (?, ?, ?)', (1,'상하이',24515000))

# 파라미터가 딕셔너리일 때는 플레이스홀더를 :<이름> 형태로 지정합니다.
c.execute('INSERT INTO cities VALUES (:rank, :city, :pop)', {'rank':2, 'city':'카라치','pop':34515000})


# excutemany() 메서드를 사용하면 여러 개의 파라미터를 리스트로 지정해서
# 여러 개 (현재 예제에서는 3개)의 SQL 구문을 실행할 수 있습니다.

c.executemany ('INSERT INTO cities VALUES (:rank, :city, :pop)',
		[{'rank':3,'city':'베이징','pop':4415000},
		{'rank':4,'city':'텐진','pop':5415000},
		{'rank':5,'city':'이스탄불','pop':6415000}
])


# 변경사항을 커밋(저장)합니다.
conn.commit()

# 저장한 데이터를 추출합니다. 
c.execute('SELECT* FROM cities')

# 쿼리의 결과는 fetchall() 메서드로 추출할 수 있습니다.
for row in c.fetchall() :
	# 추출한 데이터를 출력합니다.
	print(row)


# 연결을 닫는다.
conn.close()

