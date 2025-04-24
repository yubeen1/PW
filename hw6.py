#사용자 정의 함수
def display_multiplication_table():
    for i in range(1, 10): 
        for number in range(2, 6): 
            print(f"{number} x {i} = {number * i:2d}", end="\t")
        print(" ")
    print(" ")
    for i in range(1, 10):
        for number in range(6, 10):
            print(f"{number} x {i} = {number * i:2d}", end="\t")
        print(" ")

#주 프로그램부
display_multiplication_table()
