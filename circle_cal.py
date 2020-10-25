import math

def circle_area_circum(radius):
    area = math.pi*(radius**2)
    circum = 2 * math.pi * radius

    return area, circum


radius = int(input('반경을 입력해주세요'))

area, circum = circle_area_circum(radius)

print('반지름',radius,'인 원의 면적은', area,', 원의 둘레는', circum)