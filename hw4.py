#시용자 정의 함수부
def rep_char(c, n) :
    print(c * n)

def welcome_msg(name) :
    msg1 = "Welcome to Seoul."
    msg2 = f"Hello {name}."
    nstr = len(msg2) if (len(msg2) > len(msg1)) else len(msg1)
    rep_char("-", nstr)
    print(msg2)
    print(msg1)
    rep_char("-", nstr)

#주 프로그램부
name = input("input his/her name:")
welcome_msg(name)
