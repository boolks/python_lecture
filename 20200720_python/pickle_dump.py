import pickle

# 사용자로부터 문자열을 몇 번 입력할지 숫자를 입력 받는다.
number_of_data = int(input('Enter the number of data :'))
# 입력 받은 데이터를 저장할 list 선언
data = []

# 입력받은 숫자 만큼 for loop으로 문자열을 입력을 받는다.
for idx in range(number_of_data):
    raw = input('Enter data ' + str(idx) + ':')
    data.append(raw)

# pickle의 dump() 함수를 이용해서 문자열을 저장한 list를 저장한다.
file = open('important', 'wb')
pickle.dump(data, file)
file.close()
