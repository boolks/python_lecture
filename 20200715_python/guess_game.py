import random
guess_number = random.randint(1, 100)

print('임의의 숫자를 입력해주세요:')
num = int(input())
print(f'입력하신 숫자는 {num} 입니다.')

count = 1
while num is not guess_number:
    if num > guess_number:
        print('숫자가 너무 큽니다.')
    elif num < guess_number:
        print('숫자가 너무 작습니다.')
    else:
        break
    count += 1
    print('다시 입력해주세요.')
    num = int(input())
else:
    print(f'정답입니다. 당신은 {count}번 만에 정답을 맞추셨습니다.')
