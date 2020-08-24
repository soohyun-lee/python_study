# 다음과 같은 도시목록의 리스트가 주어졌을때, 도시이름이 S로 시작하지 않는 도시만 리스트로 만들 때 리스트 컴프리헨션을 사용하여 함수를 작성해 보세요.

cities = ["Tokyo","Shanghai","Jakarta","Seoul","Guangzhou","Beijing","Karachi","Shenzhen","Delhi" ]
not_s_city = [x for x in cities if x[0] != 'S']
print(not_s_city)

# 다음과 같은 도시, 인구수가 튜플의 리스트로 주어졌을때, 키가 도시, 값이 인구수인 딕셔너리를 딕셔너리 컴프리헨션을 사용한 함수를 작성해 보세요.

population_of_city = [('Tokyo', 36923000), ('Shanghai', 34000000), ('Jakarta', 30000000), ('Seoul', 25514000),
                      ('Guangzhou', 25000000), ('Beijing', 24900000), ('Karachi', 24300000), ( 'Shenzhen', 23300000), ('Delhi', 21753486)]

pop_city = {x:y for x,y in population_of_city}
print(pop_city)