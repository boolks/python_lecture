my_file = open('count_log.txt', 'w', encoding='utf-8')
for i in range(1, 11):
    data = '%d번 째 줄 입니다.\n' %i
    my_file.write(data)
my_file.close()

with open('count_log.txt', 'a', encoding='utf-8') as f:
    for i in range(100, 111):
        data = '%d번 째 줄입니다.\n' %i
        f.write(data)
