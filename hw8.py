#사용자 정의 함수부
def buy(lst):
    print("[구입]")
    name = input("상품명? ")
    if name != "" :
        num = input("수량은? ")
        lst[name] = num
        print(f"장바구니에 {name} {num}개가 담겼습니다.\n")
    else:
        print("")
        return False
    
def show(lst):
    print(f"장바구니 보기: {shoppingBag}\n")

def find(lst):
    print("[검색]")
    name = input("장바구니에서 확인하고자 하는 상품은? ")
    if name in lst:
        print(f"{name}은 {lst[name]}개 담겨 있습니다.")
    else:
        print(f"장바구니에 {name}은(는) 없습니다.\n")

#주 프로그램부
shoppingBag = {}
while True:
    if buy(shoppingBag) == False:
        break
show(shoppingBag)
find(shoppingBag)
