# Product 클래스 선언
class Product(object):
    # 생성자
    def __init__(self, name):
        # __name - private 변수
        self.__name = name

    def __str__(self):
        return 'Product의 이름은 {}'.format(self.__name)

    @property
    def name(self):
        return self.__name

# setter 는 getter 뒤로
    @name.setter
    def name(self, name):
        self.__name = name


# 객체생성
product = Product('텔레비전')
# getter 함수 호출
print(product.name)
# setter 함수 호출
product.name = 'TV'
print(product.name)
