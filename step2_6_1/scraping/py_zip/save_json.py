import json	


cities = [
	{'rank':1,'city':'상하이','pop':2415000},
	{'rank':2,'city':'카라치','pop':3415000},
	{'rank':3,'city':'베이징','pop':4415000},
	{'rank':4,'city':'텐진','pop':5415000},
	{'rank':5,'city':'이스탄불','pop':6415000}
]
print(json.dumps(cities))



print("\n\n\n\n\n\n\n===============================================")
print(json.dumps(cities,ensure_ascii=False, indent=2))

print("\n\n\n\n\n\n\n===============================================")

with open('top_cities.json','w') as f:
	json.dump(cities, f)
