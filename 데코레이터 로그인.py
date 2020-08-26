def login_required(func):
    def inner_function(*args, **kwargs):
        if not kwargs.get("is_login"):
            print("로그인이 되지 않아 수행하지 못합니다")
            return "로그인이 필요한 페이지 입니다."
        return func("args, **kwargs")
    return inner_function

@login_required
def login():
    print("안녕")

login()

#데코레이터가 있으면 독스트링 했을 때 함수의 속성이 사라짐
#아래를 실행하면 result : none 으로 뜨면서 함수의 속성이 사라
def login_required(func):
    def inner_function(*args, **kwargs):
        if not kwargs.get("is_login"):
            print("로그인이 되지 않아 수행하지 못합니다")
            return "로그인이 필요한 페이지 입니다."
        return func("args, **kwargs")
    return inner_function

@login_required
def login():
    """로그인 테스트 함수입니다."""
    print("안녕")

print(login.__doc__)

#개선방법

from functools import wraps  #functools 의 wraps 임포
def login_required(func):
    @wraps(func) #func으로 넘어온 값을 wraps 하면서 보존을 해줌
    def inner_function(*args, **kwargs):
        if not kwargs.get("is_login"):
            print("로그인이 되지 않아 수행하지 못합니다")
            return "로그인이 필요한 페이지 입니다."
        return func("args, **kwargs")
    return inner_function

@login_required
def login():
    print("안녕")

login()
