import feedparser
d = feedparser.parse('http://www.aladin.co.kr/rss/special_new/351')


# 항목을 순회합니다.
for entry in d.entries:
    print('이름:', entry.title)
    print('링크:',entry.link)
    print()