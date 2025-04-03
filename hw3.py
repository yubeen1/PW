#사용자 정의 함수부
def get_fixed_price(rate, discount_price) :
    result = int(discount_price / (1 - rate/100))
    return result
    

#주 프로그램부
rate = int(input("할인율은? "))
discount_price_A = int(input("A 상품의 할인된 가격은? ")) 
discount_price_B = int(input("B 상품의 할인된 가격은? "))
result_A = get_fixed_price(rate, discount_price_A)
result_B = get_fixed_price(rate, discount_price_B)
print("A 상품의 정가는", result_A, "원")
print("B 상품의 정가는", result_B, "원")


