books = list()
books.append({'제목':'개발자의 코드', '출판연도':'2013.02.28', '출판사':'A출판', '쪽수':200, '추천유무':False})
books.append({'제목':'클린 코드', '출판연도':'2013.03.04', '출판사':'B출판', '쪽수':584, '추천유무':True})
books.append({'제목':'빅데이터 마케팅', '출판연도':'2014.07.02', '출판사':'A출판', '쪽수':296, '추천유무':True})
books.append({'제목':'구글드', '출판연도':'2010.02.10', '출판사':'B출판', '쪽수':526, '추천유무':False})
books.append({'제목':'강의력', '출판연도':'2013.12.12', '출판사':'C출판', '쪽수':248, '추천유무':True})

# book_list_pages = []
# for book_page in books:
#     if book_page.get('쪽수') > 250:
#         book_list_pages.append(book_page)
# print(book_list_pages)

book_list_pages = [book_page['제목'] for book_page in books if book_page['쪽수'] > 250]
print(book_list_pages)

# book_list_pages2 = []
# for book_page in books:
#     if book_page.get('추천유무') == True:
#         book_list_pages2.append(book_page)
# print(book_list_pages2)

book_list_recommend = [book_recommend['제목'] for book_recommend in books if book_recommend['추천유무']]
print(book_list_recommend)

# book_publisher = set([])
# for publisher in books:
#     print(len(publisher.get('출판사').strip()))
#     pub = publisher.get('출판사').strip()
#     book_publisher.add(pub)
#
# print(book_publisher)

book_publisher = set([publisher.get('출판사').strip() for publisher in books])
print(book_publisher)

print('-------------------------------------------------------------')
# 책 제목 리스트
title_list = []
# 출판사 리스트
pub_comp = set()
# 쪽수가 250 초과인 리스트
many_page_list = list()
# 추천유무가 True인 리스트
recommend_list = list()
# 전체 페이지수
all_pages = int()

for book in books:
    title_list.append(book['제목'])
    pub_comp.add(book['출판사'])
    if book['쪽수'] > 250:
        many_page_list.append(book['제목'])
    if book['추천유무']:
        recommend_list.append(book['제목'])
    all_pages += book['쪽수']

print(title_list)
print(pub_comp)
print(many_page_list)
print(recommend_list)
print(all_pages)

# list Comprehension 스타일
title_list = [book['제목'] for book in books]
print(title_list)
pub_comp = set([book['출판사'] for book in books])
print(pub_comp)
many_page_list = [book['제목'] for book in books if book['쪽수'] > 250]
print(many_page_list)
recommend_list = [book['제목'] for book in books if book['추천유무']]
print(recommend_list)
all_pages = sum(book['쪽수'] for book in books)
print(all_pages)

