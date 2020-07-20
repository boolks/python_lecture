# 저장된 데이터를 읽어오기
import pickle

file = open('important', 'rb')
data = pickle.load(file)
file.close()

print('Showing the pickled data')

for idx, item in enumerate(data):
    print(idx, item)
