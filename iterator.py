l = [2,4,5,7]
print(type(l)) #<class 'list'>
l_iter = iter(l)
print(type(l_iter)) #<class 'list_iterator'>
print(next(l_iter))
print(next(l_iter)) 
#2
print(l_iter.__next__()) #4


range(5)
range(0,5)
type(range(5))
r_iter = iter(range(5))
print(next(r_iter)) #0

# 다음의 간단한 키를 출력하는 딕셔너리에 대한 for 문을 while 문으로 구현하기
D = {'a':1, 'b':2, 'c':3}
for key in D.keys():
    print(key)

D_keys = iter(D.keys())
while True:
    try:
        print(next(D_keys))
    except:
        break
