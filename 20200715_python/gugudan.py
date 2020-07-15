print('구구단 몇 단을 계산할까요?')
num = int(input())

print(f'구구단 {num}단을 계산합니다.')
while num is not 0:
    if num > 9:
        print('잘못된 숫자 입니다. 1 ~ 9 까지의 숫자를 입력하세요.')
        num = int(input())
    else:
        for i in range(1, 10):
            print('{} x {} = {}'.format(num, i, num * i))
    print('구구단을 계속 하시려면 숫자를 입력하세요. 끝내시려면 0을 입력하세요.')
    num = int(input())
else:
    print('구구단 게임을 종료합니다.')
