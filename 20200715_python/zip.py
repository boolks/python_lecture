# zip() 함수 사용하기
days = ['월요일', '화요일', '수요일']
print(type(days))
coffees = ['아메리카노', '라떼', '바닐라', '녹차']
print(zip(days, coffees))
for day, coffee in zip(days, coffees):
    print(f'{day}에는 {coffee}를 마십니다.')

print(range(10))
print(list(range(10)))

days = '월', '화', '수'
print(type(days))
coffees = '아메리카노', '라떼', '바닐라', '녹차'
print(coffees)
print(type(coffees))
print(zip(days, coffees))
print(list(zip(days, coffees)))
print(dict(zip(days, coffees)))
