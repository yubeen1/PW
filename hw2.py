#사용자 정의 함수부
def exchange(money) :

    n500 = money // 500
    money %= 500

    n100 = money //100
    money %= 100 

    n50 = money // 50
    money %= 50

    n10 = money // 10

    print("500원 동전의 개수: ", n500)
    print("100원 동전의 개수: ", n100)
    print("50원 동전의 개수: ", n50)
    print("10원 동전의 개수: ", n10)

def get_integer(prompt):
    res = int(input(prompt))
    return res

#주 프로그램부
payment = get_integer("동전으로 교환하고자 하는 금액은? ")
exchange(payment)
