shoppingBag = {}

print("[구입]")
while True:
    item = input("상품명? ")
    if item == '':
        break
    num = input("수량은? ")
    shoppingBag[item] = num
    print(f"장바구니에 {item} {num}개가 담겼습니다.\n")

print(f">>> 장바구니 보기:{shoppingBag}")

print("\n[검색]")
fItem = input("장바구니에서 확인하고자 하는 상품은? ")
if fItem in shoppingBag:
    fNum = shoppingBag.get(fItem)
    print(f"{fItem}은(는) {fNum}개 담겨 있습니다.")
else :
    print("찾으시는 상품이 장바구니에 없습니다.")
