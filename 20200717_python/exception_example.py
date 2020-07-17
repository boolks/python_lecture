# try ~ except ~ else
# try ~ except ~ finally

for i in range(10):
    try:
        result = 10 / i
    except ZeroDivisionError as err:
        print(err)
    # error 가 발생하지 않았을 때
    else:
        print(result)
    # error 에 관계없이 출력
    finally:
        print('종료되었음')
