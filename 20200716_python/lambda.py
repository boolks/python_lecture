# 일반적인 함수 정의
def add(x, y):
    return x + y


print(add(10, 20))

# lambda 함수 정의
add2 = lambda x, y: x + y
print(add2(100, 200))

# 제곱승, 곱하기 나누기 람다함수로 정의해서 호출
square = lambda x: x ** 2
multiple = lambda x, y: x * y
divide = lambda x: x / 2

print(f'제곱:{square(3)}, 곱하기:{multiple(2, 3)}, 나누기:{divide(10)}')
print(f'제곱:{(lambda x: x ** 2)(5) }, 곱하기:{(lambda x, y: x * y)(10, 4)}, 나누기:{(lambda x: int(x / 2))(50)}')

my_arr = [1, 2, 3, 4, 5]
result = map(lambda x: x * 2, my_arr)
print(result)
print(list(result))

result = list(map(lambda x: x * 2, my_arr))
print(result)

# [1, 2, 3, 4, 5] + [1, 2, 3, 4, 5]
# add(1, 1) add(2, 2) add(3, 3) add(4, 4) add(5, 5)

f_add = lambda x, y: x + y
print(f_add(1, 1))
result = list(map(f_add, my_arr, my_arr))
print(result)

# my_arr 리스트의 값을 제곱승 해서 다른 list에 저장
# lambda 함수와 map() 함수 사용
f_square = lambda x: x ** 2
result2 = map(f_square, my_arr)
for i in range(5):
    print(next(result2))

# filter 함수
result = list(filter(lambda x: x > 2, my_arr))
print(result)

for val in filter(lambda x: x > 2, my_arr):
    print(val)

# reduce
# functools.py 라는 모듈안에 있는 reduce 함수를 불러오기
from functools import reduce

result = reduce(lambda x, y: x + y, my_arr)
print(result)

