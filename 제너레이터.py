g = (x for x in range(3))
print([*g])


def gen():
    yield 1

# print(next(g),next(g,'종료'))
print('*'*69)

# gl = gen()
# for i in gl:
#     print(i)

def gen_():
    print('처리방식1')
    yield 1
    print('처리방식2')

#제너레이터 객체가 핸들러를 만들음
g2 = gen_()
print(next(g2)) #처리방식1 1
 # 호출하면 yield를 만나느 곳까지 실행, 다음 호출이 있을 때까지 yiled 문을 처리하지 않음
print(next(g2,'종료')) #처리방식2 다음 yield

print('*'*69)
def gen_1():
    for i in range(3):
        print('처리방식',i)
        yield 1
        print('처리방식',i,i+1)
g_1 = gen_1()
print(next(g_1))
print(next(g_1))
print(next(g_1))

print('*'*69)

def fact(n):
    if n in [0,1]:
        return 1
    return n * fact(n-1)

def gen_fact():
    for i in range(15):
        yield fact(i)

g_f = gen_fact()
print(next(g_f))
print(next(g_f))

print('*'*69)

import types

f = lambda x,y,z : x+y+z

print(f)
print(type(f))
print( type(f) == types.LambdaType)


print('*'*60)
lambdas = [lambda x : 'SHORT_PASSWORD' if len(x) < 8 else None,
           lambda x : 'NO_CAPITAL_LETTER_PASSWORD' if not any(c.isupper() for c in x)else None]


def check_password_using_lambda(password):

    for f in lambdas:
        if f(password) is not None:
            return f(password)

    return True


print( check_password_using_lambda('123') )            # SHORT_PASSWORD
print( check_password_using_lambda('12356789f') )      # NO_CAPITAL_LETTER_PASSWORD
print( check_password_using_lambda('123456789fF') )    # True

import types
help(types)

l = list(range(1,11))
print(l)

m = list(map(lambda n : n*n, l))
print(m)

D = {'a':1, 'b':2, 'c':3}
for key in D.keys():
    print(key)
D_keys = iter(D.keys())
while True:
    try:
        print(next(D_keys))
    except StopIteration as e:
        break



