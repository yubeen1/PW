#사용자 정의 함수부
def read_single_digit(number) :
    if number == "1" :
        res = "일"
        return res
    elif number == "2" :
        res = "이"
        return res
    elif number == "3" :
        res = "삼"
        return res
    elif number == "4" :
        res = "사"
        return res
    elif number == "5" :
        res = "오"
        return res
    elif number == "6" :
        res = "육"
        return res
    elif number == "7" :
        res = "칠"
        return res
    elif number == "8" :
        res = "팔"
        return res
    elif number == "9" :
        res = "구"
        return res
    else : return "영"

def read_number(n1, n2, n3) :
    first_word = read_single_digit(n1)
    second_word = read_single_digit(n2)
    third_word = read_single_digit(n3)
    print(first_word, second_word, third_word)

#주 프로그램부
number = input("세 자리 정수 입력: ")
n1, n2, n3 = number[0], number[1], number[2]
read_number(n1, n2, n3)
  
    
