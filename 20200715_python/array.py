# 2차원 배열
# 학생별 과목의 평균을 계산

kor_score = [49, 79, 20, 100, 80]
math_score = [43, 59, 85, 30, 90]
eng_score = [49, 79, 48, 60, 100]
midterm_score = [kor_score, math_score, eng_score]

student_score = [0, 0, 0, 0, 0]

for i in range(0, 3):
    for j in range(0, 5):
        student_score[j] += midterm_score[i][j]
else:
    a, b, c, d, e = student_score
    student_score = [int(a/3), int(b/3), int(c/3), int(d/3), int(e/3)]

    print(student_score)

student_score = [0, 0, 0, 0, 0]
idx = 0
for subject in midterm_score:
    for score in subject:
        student_score[idx] += score
        idx += 1
    idx = 0
else:
    a, b, c, d, e = student_score
    student_score = [int(a/3), int(b/3), int(c/3), int(d/3), int(e/3)]

    print(student_score)
