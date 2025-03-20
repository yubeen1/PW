#사용자 정의 함수부
def get_radius(prompt):
    r = int(input(prompt))
    return r

def get_circle_area(rad):
    area = 3.14*rad*rad
    return area

#주 프로그램부
radius = get_radius('넓이를 구하고자 하는 원의 반지름은?')
area = get_circle_area(radius)
print('반지름이', radius, '인 원의 넓이:', 3.14, 'x', radius, 'x', radius, '=', area)
