# ElementTree 모듈을 읽어 들입니다.
from xml.etree import ElementTree

# parce() 함수로 파일을 읽어 들이고 ElementTree 객체를 만듭니다.
tree = ElementTree.parse('rss.xml')

print ('---------- tree  -----------------')
print (tree)
print ('---------- tree  -----------------')
# getroot() 메서드로 XML의 루트 요소를 추출합니다. 
root = tree.getroot()
print ('---------- root  -----------------')
print (root)
print ('---------- root  -----------------')
# findall() 메서드로 요소 목록을 추출합니다.
# 태그를 찻습니다.(자세한 내용은 RSS 열어 참고해주세요.)

for item in root.findall ('channel/item/description/body/location/data') :
	# find() 메서드로 요소를 찾고 text 속성으로 값을 추출합니다.
	tm_ef = item.find('tmEf').text
	tmn = item.find('tmn').text
	tmx = item.find('tmx').text
	wf = item.find('wf').text
	print (tm_ef, tmn, tmx, wf)



