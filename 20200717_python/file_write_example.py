
import os
from random import random
from datetime import datetime
# log 디렉토리가 없으면 log 디렉토리 생성
if not os.path.isdir('log'):
    os.mkdir('log')

# file open
with open('log/count_log.txt', 'a', encoding='utf-8') as f:
    for i in range(1, 11):
        # 현재 시간 저장
        stamp = str(datetime.now())
        # random 값 저장
        value = random() * 100000
        # 현재 시간과 난수를 합해서 txt 파일에 쓰기
        result = f'시간 : {stamp}, 값 : {value}\n'
        f.write(result)
