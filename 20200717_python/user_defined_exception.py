# 사용자 정의 Exception 클래스
# 음수값이 입력되었을 때 강제로 예외를 발생시키기
class NegativePriceException(Exception):
    def __init__(self):
        print("Price can't be Negative")
        raise AttributeError


def calc_price(value):
    price = value * 1000
    if price < 0:
        raise NegativePriceException
    return price


print(calc_price(-100))
